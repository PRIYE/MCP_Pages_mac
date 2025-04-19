# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
# from pywinauto.application import Application
# import win32gui
# import win32con
import time
# from win32api import GetSystemMetrics
import subprocess
import time

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@mcp.tool()
async def draw_rectangle_mac(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Pages from (x1,y1) to (x2,y2) using Pen tool and keyboard mouse control"""
    try:
        script = f'''
        tell application "Pages"
            activate
            log "Pages activated"
            -- Create new document if none exists
            if not (exists document 1) then
                make new document
                log "New document created"
            end if
            delay 0.5
            
            tell application "System Events"
                tell process "Pages"
                    -- Wait for Pages to be frontmost with timeout
                    set timeoutCount to 0
                    repeat until frontmost
                        delay 0.1
                        set timeoutCount to timeoutCount + 1
                        if timeoutCount > 50 then
                            error "Timeout waiting for Pages to become frontmost"
                        end if
                    end repeat
                    log "Pages is frontmost"
                    
                    
                    -- Enable Mouse Keys (press Option key 5 times)
                    repeat 5 times
                        key code 58  -- Option key
                        delay 0.05
                    end repeat
                    log "Mouse Keys enabled"
                    delay 0.2
                    
                    -- Enable Pen tool (Option-Shift-Command-P)
                    keystroke "p" using {{option down, shift down, command down}}
                    delay 0.5
                    log "Pen tool enabled"
                    
                    -- Use keyboard for mouse movement with optimized delays
                    log "Starting rectangle drawing at ({x1}, {y1})"
                    
                    -- Initial position movement (batch movements for speed)
                    set batchSize to 10
                    repeat ({x1} div batchSize) times
                        repeat batchSize times
                            keystroke "o"  -- Move right
                        end repeat
                        delay 0.01
                    end repeat
                    repeat ({x1} mod batchSize) times
                        keystroke "o"  -- Move right
                    end repeat
                    log "Moved right to x position: {x1}"
                    
                    repeat ({y1} div batchSize) times
                        repeat batchSize times
                            keystroke "k"  -- Move down
                        end repeat
                        delay 0.01
                    end repeat
                    repeat ({y1} mod batchSize) times
                        keystroke "k"  -- Move down
                    end repeat
                    log "Moved down to y position: {y1}"
                    
                    -- Click to start drawing
                    keystroke "i"  -- Click
                    delay 0.1
                    log "First point set at ({x1}, {y1})"
                    
                    -- Move to second point (x2, y1) with batched movements
                    set moveRight to {x2 - x1}
                    repeat (moveRight div batchSize) times
                        repeat batchSize times
                            keystroke "o"  -- Move right
                        end repeat
                        delay 0.01
                    end repeat
                    repeat (moveRight mod batchSize) times
                        keystroke "o"  -- Move right
                    end repeat
                    keystroke "i"  -- Click
                    delay 0.1
                    log "Second point set at ({x2}, {y1})"
                    
                    -- Move to third point (x2, y2) with batched movements
                    set moveDown to {y2 - y1}
                    repeat (moveDown div batchSize) times
                        repeat batchSize times
                            keystroke "k"  -- Move down
                        end repeat
                        delay 0.01
                    end repeat
                    repeat (moveDown mod batchSize) times
                        keystroke "k"  -- Move down
                    end repeat
                    keystroke "i"  -- Click
                    delay 0.1
                    log "Third point set at ({x2}, {y2})"
                    
                    -- Move to fourth point (x1, y2) with batched movements
                    repeat (moveRight div batchSize) times
                        repeat batchSize times
                            keystroke "u"  -- Move left
                        end repeat
                        delay 0.01
                    end repeat
                    repeat (moveRight mod batchSize) times
                        keystroke "u"  -- Move left
                    end repeat
                    keystroke "i"  -- Click
                    delay 0.1
                    log "Fourth point set at ({x1}, {y2})"
                    
                    -- Close the shape by moving back to first point
                    repeat (moveDown div batchSize) times
                        repeat batchSize times
                            keystroke "8"  -- Move up
                        end repeat
                        delay 0.01
                    end repeat
                    repeat (moveDown mod batchSize) times
                        keystroke "8"  -- Move up
                    end repeat
                    keystroke "i"  -- Click
                    delay 0.1
                    log "Shape closed at starting point ({x1}, {y1})"
                    
                    -- Press Return to complete the shape
                    keystroke return
                    delay 0.2
                    log "Shape drawing completed"
                    
                    -- Disable Mouse Keys (press Option key 5 times)
                    repeat 5 times
                        key code 58  -- Option key
                        delay 0.05
                    end repeat
                    log "Mouse Keys disabled"
                    
                    -- Exit Pen tool (Escape key)
                    key code 53
                    log "Pen tool disabled"
                    
                    log "Drawing operation completed successfully"
                end tell
            end tell
        end tell
        '''
        
        print("Starting rectangle drawing operation...")
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=60)  # Add 60-second timeout
        
        if result.returncode != 0:
            print(f"Error in AppleScript execution: {result.stderr}")
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Error executing AppleScript: {result.stderr}"
                    )
                ]
            }
        
        print("AppleScript output:")
        print(result.stdout)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn successfully using Pen tool and keyboard mouse control from ({x1},{y1}) to ({x2},{y2}) in full screen mode\nCheck terminal for detailed operation logs."
                )
            ]
        }
    except subprocess.TimeoutExpired:
        print("Operation timed out after 60 seconds")
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Operation timed out after 60 seconds. Please try again with smaller coordinates or check if Pages is responding."
                )
            ]
        }
    except Exception as e:
        print(f"Python exception occurred: {str(e)}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def draw_rectangle_and_text_mac(text: str) -> dict:
    """Draw a rectangle and add text in Pages"""
    try:
        # AppleScript to draw rectangle and add text in Pages with full screen
        script = f'''
        tell application "Pages"
            activate
            -- Create new document if none exists
            if not (exists document 1) then
                make new document
            end if
            delay 1
            
            tell application "System Events"
                -- Get screen resolution
                tell process "Pages"
                    set screenSize to get size of window 1
                    
                    -- Enter full screen mode (Command + Control + F)
                    keystroke "f" using {{command down, control down}}
                    delay 2
                    
                    -- Wait for Pages to be frontmost
                    repeat until frontmost
                        delay 0.1
                    end repeat
                    
                    -- Click Insert in the menu bar
                    click menu bar item "Insert" of menu bar 1
                    delay 1
                    
                    -- Click Shape in the Insert menu
                    tell menu 1 of menu bar item "Insert" of menu bar 1
                        click menu item "Shape"
                        delay 0.5
                        
                        -- Click Rectangle in the Shape menu
                        tell menu 1 of menu item "Shape"
                            click menu item "Rectangle"
                        end tell
                    end tell
                    delay 1
                    
                    -- Open Format sidebar if not already open
                    keystroke "cmd" using {{command down}}
                    delay 0.5
                    
                    -- Click Arrange tab in Format sidebar
                    click button "Arrange" of group 1 of window 1
                    delay 0.5
                    
                    -- Set position and size for rectangle
                    set value of text field "X" to "100"
                    delay 0.2
                    set value of text field "Y" to "100"
                    delay 0.2
                    set value of text field "Width" to "200"
                    delay 0.2
                    set value of text field "Height" to "100"
                    delay 0.2
                    
                    -- Press Return to apply changes
                    keystroke return
                    delay 0.5
                    
                    -- Add text box
                    click menu bar item "Insert" of menu bar 1
                    delay 0.5
                    
                    -- Click Text Box in the Insert menu
                    tell menu 1 of menu bar item "Insert" of menu bar 1
                        click menu item "Text Box"
                    end tell
                    delay 0.5
                    
                    -- Position text box in the middle of the rectangle
                    set value of text field "X" to "150"
                    delay 0.2
                    set value of text field "Y" to "130"
                    delay 0.2
                    
                    -- Add text
                    keystroke "{text}"
                end tell
            end tell
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        
        if result.returncode != 0:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Error executing AppleScript: {result.stderr}"
                    )
                ]
            }
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn and text '{text}' added successfully with precise positioning"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_paint_mac() -> dict:
    """Open Pages on macOS"""
    try:
        script = '''
        tell application "Pages"
            activate
            -- Create new document if none exists
            if not (exists document 1) then
                make new document
            end if
            
            -- Exit full screen if needed
            tell application "System Events"
                keystroke "f" using {control down, command down}
                delay 1
            end tell
            
            -- Ensure window is at a good size
            set bounds of window 1 to {100, 100, 1000, 800}
            delay 1
            
            tell application "System Events"
                tell process "Pages"
                    -- Wait for Pages to be frontmost
                    repeat until frontmost
                        delay 0.1
                    end repeat
                end tell
            end tell
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        
        if result.returncode != 0:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Error executing AppleScript: {result.stderr}"
                    )
                ]
            }
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Pages opened successfully in window mode"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Pages: {str(e)}"
                )
            ]
        }

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
