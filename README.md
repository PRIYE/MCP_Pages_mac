# MCP Pages Mac - Mathematical Calculations & Visualization

A Python-based application that performs mathematical calculations and visualizes results in Apple Pages using the Model Context Protocol (MCP) framework. The application combines mathematical operations with automated Pages document creation and manipulation.

## Video [Youtube](https://www.youtube.com/watch?v=EHZp3ipjlBw) 

## Usage Example

```python
# Example: Calculate ASCII values of "INDIA" and display result
query = """Find the ASCII values of characters in INDIA and then calculate sum of exponentials of those values.
Now open Pages and write this value inside a rectangle. Rectangle coordinates should be 100 x 100 and 500 x 400. 
Now, Send the value to email priyeindia20@gmail.com """

# Run the application
python pages_mcp_client.py
```

## Logs 
 ```
 (mcp) priye@Priyes-MacBook-Air Session4  % python pages_mcp_client.py
Starting main execution...
[2025-05-10 03:51:33] INFO: Establishing connection to MCP server...
[2025-05-10 03:51:33] INFO: Connection established, creating session...
[2025-05-10 03:51:33] INFO: Session created, initializing...
[2025-05-10 03:51:34] INFO: Requesting tool list...
[05/10/25 03:51:34] INFO     Processing request of type ListToolsRequest                                            server.py:534
[2025-05-10 03:51:34] INFO: Successfully retrieved 22 tools
[2025-05-10 03:51:34] INFO: Creating system prompt...
[2025-05-10 03:51:34] INFO: Number of tools: 22
[2025-05-10 03:51:34] DEBUG: Added description for tool: 1. add(a: integer, b: integer) - Add two numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 2. add_list(l: array) - Add all numbers in a list
[2025-05-10 03:51:34] DEBUG: Added description for tool: 3. subtract(a: integer, b: integer) - Subtract two numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 4. multiply(a: integer, b: integer) - Multiply two numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 5. divide(a: integer, b: integer) - Divide two numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 6. power(a: integer, b: integer) - Power of two numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 7. sqrt(a: integer) - Square root of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 8. cbrt(a: integer) - Cube root of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 9. factorial(a: integer) - factorial of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 10. log(a: integer) - log of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 11. remainder(a: integer, b: integer) - remainder of two numbers divison
[2025-05-10 03:51:34] DEBUG: Added description for tool: 12. sin(a: integer) - sin of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 13. cos(a: integer) - cos of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 14. tan(a: integer) - tan of a number
[2025-05-10 03:51:34] DEBUG: Added description for tool: 15. mine(a: integer, b: integer) - special mining tool
[2025-05-10 03:51:34] DEBUG: Added description for tool: 16. create_thumbnail(image_path: string) - Create a thumbnail from an image
[2025-05-10 03:51:34] DEBUG: Added description for tool: 17. strings_to_chars_to_int(string: string) - Return the ASCII values of the characters in a word
[2025-05-10 03:51:34] DEBUG: Added description for tool: 18. int_list_to_exponential_sum(int_list: array) - Return sum of exponentials of numbers in a list
[2025-05-10 03:51:34] DEBUG: Added description for tool: 19. fibonacci_numbers(n: integer) - Return the first n Fibonacci Numbers
[2025-05-10 03:51:34] DEBUG: Added description for tool: 20. draw_rectangle_mac(x1: integer, y1: integer, x2: integer, y2: integer) - Open Pages and Draw a rectangle box in Pages from (x1,y1) to (x2,y2)
[2025-05-10 03:51:34] DEBUG: Added description for tool: 21. add_text_to_rectangle_mac(x1: integer, y1: integer, x2: integer, y2: integer, text: string) - Add text to a rectangle in Pages
[2025-05-10 03:51:34] DEBUG: Added description for tool: 22. send_email_report(recipient: string, final_result: string) - Sends an email report to recipient email containing final result
[2025-05-10 03:51:34] INFO: Successfully created tools description
[2025-05-10 03:51:34] INFO: System prompt created successfully
Starting iteration loop...
[2025-05-10 03:51:34] INFO: 
--- Iteration 1 ---
[2025-05-10 03:51:34] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:51:35] INFO: LLM Response: FUNCTION_CALL: strings_to_chars_to_int|INDIA
[2025-05-10 03:51:35] DEBUG: Raw function info:  strings_to_chars_to_int|INDIA
[2025-05-10 03:51:35] DEBUG: Function name: strings_to_chars_to_int
[2025-05-10 03:51:35] DEBUG: Raw parameters: ['INDIA']
[2025-05-10 03:51:35] DEBUG: Found tool: strings_to_chars_to_int
[2025-05-10 03:51:35] DEBUG: Tool schema: {'properties': {'string': {'title': 'String', 'type': 'string'}}, 'required': ['string'], 'title': 'strings_to_chars_to_intArguments', 'type': 'object'}
DEBUG: Schema properties: {'string': {'title': 'String', 'type': 'string'}}
DEBUG: Converting parameter string with value INDIA to type string
DEBUG: Final arguments: {'string': 'INDIA'}
DEBUG: Calling tool strings_to_chars_to_int
[05/10/25 03:51:35] INFO     Processing request of type CallToolRequest                                             server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='78', annotations=None), TextContent(type='text', text='68', annotations=None), TextContent(type='text', text='73', annotations=None), TextContent(type='text', text='65', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['73', '78', '68', '73', '65']
[2025-05-10 03:51:37] INFO: 
--- Iteration 2 ---
[2025-05-10 03:51:37] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:51:38] INFO: LLM Response: FUNCTION_CALL: int_list_to_exponential_sum|[73, 78, 68, 73, 65]
[2025-05-10 03:51:38] DEBUG: Raw function info:  int_list_to_exponential_sum|[73, 78, 68, 73, 65]
[2025-05-10 03:51:38] DEBUG: Function name: int_list_to_exponential_sum
[2025-05-10 03:51:38] DEBUG: Raw parameters: ['[73, 78, 68, 73, 65]']
[2025-05-10 03:51:38] DEBUG: Found tool: int_list_to_exponential_sum
[2025-05-10 03:51:38] DEBUG: Tool schema: {'properties': {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}, 'required': ['int_list'], 'title': 'int_list_to_exponential_sumArguments', 'type': 'object'}
DEBUG: Schema properties: {'int_list': {'items': {}, 'title': 'Int List', 'type': 'array'}}
DEBUG: Converting parameter int_list with value [73, 78, 68, 73, 65] to type array
DEBUG: Final arguments: {'int_list': [73, 78, 68, 73, 65]}
DEBUG: Calling tool int_list_to_exponential_sum
[05/10/25 03:51:38] INFO     Processing request of type CallToolRequest                                             server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='7.59982224609308e+33', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['7.59982224609308e+33']
[2025-05-10 03:51:40] INFO: 
--- Iteration 3 ---
[2025-05-10 03:51:40] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:51:41] INFO: LLM Response: FUNCTION_CALL: draw_rectangle_mac|100|100|500|400
[2025-05-10 03:51:41] DEBUG: Raw function info:  draw_rectangle_mac|100|100|500|400
[2025-05-10 03:51:41] DEBUG: Function name: draw_rectangle_mac
[2025-05-10 03:51:41] DEBUG: Raw parameters: ['100', '100', '500', '400']
[2025-05-10 03:51:41] DEBUG: Found tool: draw_rectangle_mac
[2025-05-10 03:51:41] DEBUG: Tool schema: {'properties': {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}}, 'required': ['x1', 'y1', 'x2', 'y2'], 'title': 'draw_rectangle_macArguments', 'type': 'object'}
DEBUG: Schema properties: {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}}
DEBUG: Converting parameter x1 with value 100 to type integer
DEBUG: Converting parameter y1 with value 100 to type integer
DEBUG: Converting parameter x2 with value 500 to type integer
DEBUG: Converting parameter y2 with value 400 to type integer
DEBUG: Final arguments: {'x1': 100, 'y1': 100, 'x2': 500, 'y2': 400}
DEBUG: Calling tool draw_rectangle_mac
[05/10/25 03:51:41] INFO     Processing request of type CallToolRequest                                             server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='{"content": [{"type": "text", "text": "Rectangle drawn successfully using PyAutoGUI from (100,100) to (500,400)", "annotations": null}]}', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['{"content": [{"type": "text", "text": "Rectangle drawn successfully using PyAutoGUI from (100,100) to (500,400)", "annotations": null}]}']
[2025-05-10 03:51:55] INFO: 
--- Iteration 4 ---
[2025-05-10 03:51:55] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:51:56] INFO: LLM Response: FUNCTION_CALL: add_text_to_rectangle_mac|100|100|500|400|7.59982224609308e+33
[2025-05-10 03:51:56] DEBUG: Raw function info:  add_text_to_rectangle_mac|100|100|500|400|7.59982224609308e+33
[2025-05-10 03:51:56] DEBUG: Function name: add_text_to_rectangle_mac
[2025-05-10 03:51:56] DEBUG: Raw parameters: ['100', '100', '500', '400', '7.59982224609308e+33']
[2025-05-10 03:51:56] DEBUG: Found tool: add_text_to_rectangle_mac
[2025-05-10 03:51:56] DEBUG: Tool schema: {'properties': {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}, 'text': {'title': 'Text', 'type': 'string'}}, 'required': ['x1', 'y1', 'x2', 'y2', 'text'], 'title': 'add_text_to_rectangle_macArguments', 'type': 'object'}
DEBUG: Schema properties: {'x1': {'title': 'X1', 'type': 'integer'}, 'y1': {'title': 'Y1', 'type': 'integer'}, 'x2': {'title': 'X2', 'type': 'integer'}, 'y2': {'title': 'Y2', 'type': 'integer'}, 'text': {'title': 'Text', 'type': 'string'}}
DEBUG: Converting parameter x1 with value 100 to type integer
DEBUG: Converting parameter y1 with value 100 to type integer
DEBUG: Converting parameter x2 with value 500 to type integer
DEBUG: Converting parameter y2 with value 400 to type integer
DEBUG: Converting parameter text with value 7.59982224609308e+33 to type string
DEBUG: Final arguments: {'x1': 100, 'y1': 100, 'x2': 500, 'y2': 400, 'text': '7.59982224609308e+33'}
DEBUG: Calling tool add_text_to_rectangle_mac
[05/10/25 03:51:56] INFO     Processing request of type CallToolRequest                                             server.py:534
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='{"content": [{"type": "text", "text": "Text created and moved to center position (432, 225) with text \'7.59982224609308e+33\'", "annotations": null}]}', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['{"content": [{"type": "text", "text": "Text created and moved to center position (432, 225) with text \'7.59982224609308e+33\'", "annotations": null}]}']
[2025-05-10 03:52:08] INFO: 
--- Iteration 5 ---
[2025-05-10 03:52:08] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:52:10] INFO: LLM Response: FUNCTION_CALL: send_email_report|priyeindia20@gmail.com|7.59982224609308e+33
[2025-05-10 03:52:10] DEBUG: Raw function info:  send_email_report|priyeindia20@gmail.com|7.59982224609308e+33
[2025-05-10 03:52:10] DEBUG: Function name: send_email_report
[2025-05-10 03:52:10] DEBUG: Raw parameters: ['priyeindia20@gmail.com', '7.59982224609308e+33']
[2025-05-10 03:52:10] DEBUG: Found tool: send_email_report
[2025-05-10 03:52:10] DEBUG: Tool schema: {'properties': {'recipient': {'title': 'Recipient', 'type': 'string'}, 'final_result': {'title': 'Final Result', 'type': 'string'}}, 'required': ['recipient', 'final_result'], 'title': 'send_email_reportArguments', 'type': 'object'}
DEBUG: Schema properties: {'recipient': {'title': 'Recipient', 'type': 'string'}, 'final_result': {'title': 'Final Result', 'type': 'string'}}
DEBUG: Converting parameter recipient with value priyeindia20@gmail.com to type string
DEBUG: Converting parameter final_result with value 7.59982224609308e+33 to type string
DEBUG: Final arguments: {'recipient': 'priyeindia20@gmail.com', 'final_result': '7.59982224609308e+33'}
DEBUG: Calling tool send_email_report
[05/10/25 03:52:10] INFO     Processing request of type CallToolRequest                                             server.py:534
send: 'ehlo 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa\r\n'
reply: b'250-smtp.gmail.com at your service, [104.28.225.14]\r\n'
reply: b'250-SIZE 35882577\r\n'
reply: b'250-8BITMIME\r\n'
reply: b'250-STARTTLS\r\n'
reply: b'250-ENHANCEDSTATUSCODES\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-CHUNKING\r\n'
reply: b'250 SMTPUTF8\r\n'
reply: retcode (250); Msg: b'smtp.gmail.com at your service, [104.28.225.14]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8'
send: 'STARTTLS\r\n'
reply: b'220 2.0.0 Ready to start TLS\r\n'
reply: retcode (220); Msg: b'2.0.0 Ready to start TLS'
send: 'ehlo 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa\r\n'
reply: b'250-smtp.gmail.com at your service, [104.28.225.14]\r\n'
reply: b'250-SIZE 35882577\r\n'
reply: b'250-8BITMIME\r\n'
reply: b'250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\r\n'
reply: b'250-ENHANCEDSTATUSCODES\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-CHUNKING\r\n'
reply: b'250 SMTPUTF8\r\n'
reply: retcode (250); Msg: b'smtp.gmail.com at your service, [104.28.225.14]\nSIZE 35882577\n8BITMIME\nAUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8'
send: 'AUTH PLAIN AHByaXllaW5kaWEyMEBnbWFpbC5jb20AbXd5ZCBleHF0IGJ5YWkgeWx2Zg==\r\n'
reply: b'235 2.7.0 Accepted\r\n'
reply: retcode (235); Msg: b'2.7.0 Accepted'
send: 'mail from:<priyeindia20@gmail.com> size=491\r\n'
reply: b'250 2.1.0 OK d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp\r\n'
reply: retcode (250); Msg: b'2.1.0 OK d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp'
send: 'rcpt to:<priyeindia20@gmail.com>\r\n'
reply: b'250 2.1.5 OK d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp\r\n'
reply: retcode (250); Msg: b'2.1.5 OK d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp'
send: 'data\r\n'
reply: b'354 Go ahead d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp\r\n'
reply: retcode (354); Msg: b'Go ahead d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp'
data: (354, b'Go ahead d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp')
send: b'Content-Type: multipart/mixed; boundary="===============2045616197427544481=="\r\nMIME-Version: 1.0\r\nFrom: priyeindia20@gmail.com\r\nTo: priyeindia20@gmail.com\r\nSubject: Pages MCP Agent Execution\r\n\r\n--===============2045616197427544481==\r\nContent-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\n\r\n\r\n                Pages MCP Agent Execution\r\n\r\n                 Result: 7.59982224609308e+33\r\n\r\n                \r\n--===============2045616197427544481==--\r\n.\r\n'
reply: b'250 2.0.0 OK  1746829334 d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp\r\n'
reply: retcode (250); Msg: b'2.0.0 OK  1746829334 d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp'
data: (250, b'2.0.0 OK  1746829334 d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp')
send: 'quit\r\n'
reply: b'221 2.0.0 closing connection d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp\r\n'
reply: retcode (221); Msg: b'2.0.0 closing connection d9443c01a7336-22fc75468e4sm22683125ad.44 - gsmtp'
DEBUG: Raw result: meta=None content=[TextContent(type='text', text='{"content": ["Email report sent successfully to priyeindia20@gmail.com"]}', annotations=None)] isError=False
DEBUG: Result has content attribute
DEBUG: Final iteration result: ['{"content": ["Email report sent successfully to priyeindia20@gmail.com"]}']
[2025-05-10 03:52:16] INFO: 
--- Iteration 6 ---
[2025-05-10 03:52:16] INFO: Preparing to generate LLM response...
Starting LLM generation...
LLM generation completed
[2025-05-10 03:52:17] INFO: LLM Response: FINAL_ANSWER: [7.59982224609308e+33]
[2025-05-10 03:52:17] INFO: === Agent Execution Complete ===
Final result: 7.59982224609308e+33

 ```

## Features

- Mathematical Operations
  - Basic arithmetic (add, subtract, multiply, divide)
  - Advanced math (power, square root, cube root, factorial, logarithm)
  - Special operations (ASCII value conversion, exponential sums)
  - List operations (sum of lists)

- Visualization in Pages
  - Automatic Pages document creation
  - Rectangle drawing with specified coordinates
  - Text insertion and formatting
  - Dynamic positioning based on screen resolution

- System Integration
  - AppleScript automation
  - PyAutoGUI for mouse and keyboard control
  - Email reporting functionality
  - Logging system

## Prerequisites

- macOS (tested on macOS 23.5.0)
- Python 3.x
- Apple Pages
- Google Gemini API access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd MCP_Pages_mac
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```plaintext
GEMINI_API_KEY=your_api_key_here
GMAIL_USER=your_email_here
```

## Project Structure

- `pages_mcp_client.py`: Main client application
  - Handles user interactions
  - Manages MCP server communication
  - Processes mathematical operations
  - Controls Pages automation

- `pages_mcp_server.py`: Server component
  - Defines available tools and operations
  - Implements mathematical functions
  - Manages Pages document manipulation
  - Handles email reporting

## Available Tools

1. Mathematical Operations:
   - `add(a: int, b: int)`: Add two numbers
   - `subtract(a: int, b: int)`: Subtract two numbers
   - `multiply(a: int, b: int)`: Multiply two numbers
   - `divide(a: int, b: int)`: Divide two numbers
   - `power(a: int, b: int)`: Calculate power
   - `sqrt(a: int)`: Calculate square root
   - `factorial(a: int)`: Calculate factorial
   - `log(a: int)`: Calculate natural logarithm

2. String Operations:
   - `strings_to_chars_to_int(string: str)`: Convert string to ASCII values

3. Pages Operations:
   - `open_pages_mac()`: Open Pages application
   - `draw_rectangle_mac(x1: int, y1: int, x2: int, y2: int)`: Draw rectangle
   - `add_text_to_rectangle_mac(x1: int, y1: int, x2: int, y2: int, text: str)`: Add text to rectangle

## Workflow

1. Mathematical calculation is performed
2. Pages application is opened
3. Rectangle is drawn at specified coordinates
4. Result is displayed inside the rectangle
5. Email report is generated (if configured)

## Error Handling

- Comprehensive logging system
- Exception handling for:
  - Mathematical operations
  - Pages automation
  - File operations
  - API calls

## Configuration

- `pyautogui.FAILSAFE = True`: Safety feature for mouse control
- `pyautogui.PAUSE = 0.1`: Delay between actions
- Configurable timeout for LLM operations (default: 10 seconds)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Your License Here]

## Acknowledgments

- MCP Framework
- Google Gemini API
- PyAutoGUI
- Apple Pages
