import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
from google import genai
from concurrent.futures import TimeoutError
from functools import partial
import sys
import datetime
import time
# Load environment variables from .env file
load_dotenv()

# Access your API key and initialize Gemini client correctly
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

max_iterations = 10
last_response = None
iteration = 0
iteration_response = []

# Replace the simple log_execution function with an enhanced logging system
class Logger:
    def __init__(self):
        self.logs = []
        self._original_stdout = sys.stdout
        
    def log(self, message: str, level: str = "INFO"):
        """Add message to execution logs and print it"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def debug(self, message: str):
        self.log(message, "DEBUG")
    
    def info(self, message: str):
        self.log(message, "INFO")
    
    def error(self, message: str):
        self.log(message, "ERROR")
    
    def get_logs(self) -> list[str]:
        return self.logs

# Create global logger instance
logger = Logger()


async def generate_with_timeout(client, prompt, timeout=10):
    """Generate content with a timeout"""
    print("Starting LLM generation...")
    try:
        # Convert the synchronous generate_content call to run in a thread
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            loop.run_in_executor(
                None, 
                lambda: client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
            ),
            timeout=timeout
        )
        print("LLM generation completed")
        return response
    except TimeoutError:
        print("LLM generation timed out!")
        raise
    except Exception as e:
        print(f"Error in LLM generation: {e}")
        raise

def reset_state():
    """Reset all global variables to their initial state"""
    global last_response, iteration, iteration_response
    last_response = None
    iteration = 0
    iteration_response = []

async def main():
    reset_state()  # Reset at the start of main
    print("Starting main execution...")
    try:
        # Create a single MCP server connection
        logger.info("Establishing connection to MCP server...")
        server_params = StdioServerParameters(
            command="python",
            args=["pages_mcp_server.py"]
        )

        async with stdio_client(server_params) as (read, write):
            logger.info("Connection established, creating session...")
            async with ClientSession(read, write) as session:
                logger.info("Session created, initializing...")
                await session.initialize()
                
                # Get available tools
                logger.info("Requesting tool list...")
                tools_result = await session.list_tools()
                tools = tools_result.tools
                logger.info(f"Successfully retrieved {len(tools)} tools")

                # Create system prompt with available tools
                logger.info("Creating system prompt...")
                logger.info(f"Number of tools: {len(tools)}")
                
                try:
                    # Create system prompt with available tools
                    tools_description = []
                    for i, tool in enumerate(tools):
                            try:
                                # Get tool properties
                                params = tool.inputSchema
                                desc = getattr(tool, 'description', 'No description available')
                                name = getattr(tool, 'name', f'tool_{i}')
                                # Format the input schema in a more readable way
                                if 'properties' in params:
                                    param_details = []
                                    for param_name, param_info in params['properties'].items():
                                        param_type = param_info.get('type', 'unknown')
                                        param_details.append(f"{param_name}: {param_type}")
                                    params_str = ', '.join(param_details)
                                else:
                                    params_str = 'no parameters'
                                tool_desc = f"{i+1}. {name}({params_str}) - {desc}"
                                tools_description.append(tool_desc)
                                logger.debug(f"Added description for tool: {tool_desc}")
                            except Exception as e:
                                logger.error(f"Error processing tool {i}: {e}")
                                tools_description.append(f"{i+1}. Error processing tool")
                    tools_description = "\n".join(tools_description)
                    logger.info("Successfully created tools description")
                except Exception as e:  
                    logger.error(f"Error creating tools description: {e}")
                    tools_description = "No tools available"

                # Create system prompt with tools description
                system_prompt = f"""
                You are a helpful assistant that can solve maths problems and then present the results using the following tools:
                {tools_description}
                
                You must respond with EXACTLY ONE line in one of these formats (no additional text):
                1. For function calls:
                   FUNCTION_CALL: function_name|param1|param2|...
                
                2. For final answers:
                   FINAL_ANSWER: [number]
                   
                   
                Workflow:
                    1. Perform calculation
                    2. Handle any errors
                    3. Calculate dynamic positioning
                    4. Open Pages
                    5. Draw rectangle with proper formatting using (x1, y1) and (x2, y2) 
                    6. Add formatted text to the above rectangle in Pages
                    7. Send email report
                
                Important:
                - When a function returns multiple values, you need to process all of them
                - Only give FINAL_ANSWER when you have completed all necessary calculations
                - Do not repeat function calls with the same parameters
                
                Examples:
                - FUNCTION_CALL: add|5|3
                - FUNCTION_CALL: strings_to_chars_to_int|INDIA
                - FINAL_ANSWER: [42]
                - FUNCTION_CALL: open_pages_mac
                - FUNCTION_CALL: draw_rectangle_mac|100|100|300|200
                - FUNCTION_CALL: add_text_to_rectangle_mac|100|100|300|200|42
                
                You will be given a task to execute. You need to use the available tools to complete the task.
                """



                logger.info("System prompt created successfully")
                
                query = """
                Find the ASCII values of characters in INDIA and then calculate sum of exponentials of those values.
                Now open Pages and write this value inside a rectangle. Rectangle coordinates should be 100 x 100 and 500 x 400. 
                Now, Send the value to email priyeindia20@gmail.com """
                print("Starting iteration loop...")
                
                # Use global iteration variables
                global iteration, last_response
                
                while iteration < max_iterations:
                    logger.info(f"\n--- Iteration {iteration + 1} ---")
                    if last_response is None:
                        current_query = query
                    else:
                        current_query = current_query + "\n\n" + " ".join(iteration_response)
                        current_query = current_query + "  What should I do next?"

                    # Get model's response with timeout
                    logger.info("Preparing to generate LLM response...")
                    prompt = f"{system_prompt}\n\nQuery: {current_query}"
                    try:
                        response = await generate_with_timeout(client, prompt)
                        response_text = response.text.strip()
                        logger.info(f"LLM Response: {response_text}")
                        
                        # Find the FUNCTION_CALL line in the response
                        for line in response_text.split('\n'):
                            line = line.strip()
                            if line.startswith("FUNCTION_CALL:"):
                                response_text = line
                                break
                        
                    except Exception as e:
                        print(f"Failed to get LLM response: {e}")
                        break


                    if response_text.startswith("FUNCTION_CALL:"):
                        _, function_info = response_text.split(":", 1)
                        parts = [p.strip() for p in function_info.split("|")]
                        func_name, params = parts[0], parts[1:]
                        
                        logger.debug(f"Raw function info: {function_info}")
                        logger.debug(f"Function name: {func_name}")
                        logger.debug(f"Raw parameters: {params}")
                        
                        try:
                            # Find the matching tool to get its input schema
                            tool = next((t for t in tools if t.name == func_name), None)
                            if not tool:
                                logger.debug(f"Available tools: {[t.name for t in tools]}")
                                raise ValueError(f"Unknown tool: {func_name}")

                            logger.debug(f"Found tool: {tool.name}")
                            logger.debug(f"Tool schema: {tool.inputSchema}")

                            # Prepare arguments according to the tool's input schema
                            arguments = {}
                            schema_properties = tool.inputSchema.get('properties', {})
                            print(f"DEBUG: Schema properties: {schema_properties}")

                            for param_name, param_info in schema_properties.items():
                                if not params:  # Check if we have enough parameters
                                    raise ValueError(f"Not enough parameters provided for {func_name}")
                                    
                                value = params.pop(0)  # Get and remove the first parameter
                                param_type = param_info.get('type', 'string')
                                
                                print(f"DEBUG: Converting parameter {param_name} with value {value} to type {param_type}")
                                
                                # Convert the value to the correct type based on the schema
                                if param_type == 'integer':
                                    arguments[param_name] = int(value)
                                elif param_type == 'number':
                                    arguments[param_name] = float(value)
                                elif param_type == 'array':
                                    # Handle array input
                                    if isinstance(value, str):
                                        value = value.strip('[]').split(',')
                                    arguments[param_name] = [int(x.strip()) for x in value]
                                else:
                                    arguments[param_name] = str(value)

                            print(f"DEBUG: Final arguments: {arguments}")
                            print(f"DEBUG: Calling tool {func_name}")
                            
                            result = await session.call_tool(func_name, arguments=arguments)
                            await asyncio.sleep(2)
                            print(f"DEBUG: Raw result: {result}")
                            
                            # Get the full result content
                            if hasattr(result, 'content'):
                                print(f"DEBUG: Result has content attribute")
                                # Handle multiple content items
                                if isinstance(result.content, list):
                                    iteration_result = [
                                        item.text if hasattr(item, 'text') else str(item)
                                        for item in result.content
                                    ]
                                else:
                                    iteration_result = str(result.content)
                            else:
                                print(f"DEBUG: Result has no content attribute")
                                iteration_result = str(result)
                                
                            print(f"DEBUG: Final iteration result: {iteration_result}")
                            
                            # Format the response based on result type
                            if isinstance(iteration_result, list):
                                result_str = f"[{', '.join(iteration_result)}]"
                            else:
                                result_str = str(iteration_result)
                            
                            iteration_response.append(
                                f"In the {iteration + 1} iteration you called {func_name} with {arguments} parameters, "
                                f"and the function returned {result_str}."
                            )
                            last_response = iteration_result

                        except Exception as e:
                            logger.error(f"Error details: {str(e)}")
                            logger.error(f"Error type: {type(e)}")
                            import traceback
                            logger.error(traceback.format_exc())
                            iteration_response.append(f"Error in iteration {iteration + 1}: {str(e)}")
                            break

                    elif response_text.startswith("FINAL_ANSWER:"):
                        final_result = response_text.split("[")[1].split("]")[0]
                        
                        # Add final execution log
                        logger.info("=== Agent Execution Complete ===")
                        
                        # # Create Word document and draw rectangle with result
                        # word_result = await session.call_tool("open_word")
                        # logger.info(f"Word document creation: {word_result}")
                        
                        # rectangle_result = await session.call_tool(
                        #     "draw_word_rectangle_with_text",
                        #     arguments={"text": f"Final Answer: {final_result}"}
                        # )
                        # logger.info(f"Rectangle creation: {rectangle_result}")
                        
                        # # Send email report with complete logs
                        # recipient_email = os.getenv("GMAIL_USER")
                        # email_result = await session.call_tool(
                        #     "send_email_report",
                        #     arguments={
                        #         "recipient": recipient_email,
                        #         "logs": logger.get_logs(),  # Use collected logs
                        #         "final_result": final_result
                        #     }
                        # )
                        # logger.info(f"Email report: {email_result}")
                        
                        print(f"Final result: {final_result}")
                        break

                    iteration += 1

    except Exception as e:
        print(f"Error in main execution: {e}")
        import traceback
        traceback.print_exc()
    finally:
        reset_state()  # Reset at the end of main

if __name__ == "__main__":
    asyncio.run(main())