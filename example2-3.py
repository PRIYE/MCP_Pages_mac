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
import pyautogui

# Configure PyAutoGUI settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1  # Add small delay between actions

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
    """Draw a rectangle in Pages from (x1,y1) to (x2,y2) using PyAutoGUI"""
    try:
        print("Starting rectangle drawing operation...")
        
        # # Activate Pages
        # subprocess.run(['open', '-a', 'Pages'])
        # time.sleep(1)  # Wait for Pages to open
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
                    -- Enter full screen mode (Command + Control + F)
                    keystroke "f" using {{command down, control down}}
                    delay 1
                    log "Entered full screen mode"
                    
                    -- Set zoom to Fit Page (Command + 0)
                    keystroke "0" using {{command down}}
                    delay 1
                    log "Set zoom to Fit Page"

                    -- Enable Pen tool (Option-Shift-Command-P)
                    keystroke "p" using {{option down, shift down, command down}}
                    delay 0.5
                    log "Pen tool enabled"
                end tell
            end tell
        end tell
        '''

        print("Starting rectangle drawing operation...")
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=60)  # Add 60-second timeout
        # Get screen size
        screen_width, screen_height = pyautogui.size()
        print(f"Screen size: {screen_width}x{screen_height}")
        
        # Calculate actual coordinates based on screen size
        def scale_coord(coord, max_val):
            return int((coord / 1000) * max_val)
        
        # Scale coordinates to screen size
        x1_scaled = scale_coord(x1, screen_width)
        y1_scaled = scale_coord(y1, screen_height)
        x2_scaled = scale_coord(x2, screen_width)
        y2_scaled = scale_coord(y2, screen_height)
        
        print(f"Scaled coordinates: ({x1_scaled}, {y1_scaled}) to ({x2_scaled}, {y2_scaled})")
        print("Pen tool menu not found, trying keyboard shortcut")
        # Draw rectangle
        print("Drawing rectangle...")
        
        # Move to first point
        pyautogui.moveTo(x1_scaled, y1_scaled, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        
        # Move to second point
        pyautogui.moveTo(x2_scaled, y1_scaled, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        
        # Move to third point
        pyautogui.moveTo(x2_scaled, y2_scaled, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        
        # Move to fourth point
        pyautogui.moveTo(x1_scaled, y2_scaled, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        
        # Close shape by returning to first point
        pyautogui.moveTo(x1_scaled, y1_scaled, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        
        # Press Return to complete the shape
        pyautogui.press('return')
        time.sleep(0.2)
        
        # Exit Pen tool with Escape
        pyautogui.press('esc')
        
        print("Rectangle drawing completed")
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn successfully using PyAutoGUI from ({x1},{y1}) to ({x2},{y2})"
                )
            ]
        }
        
    except Exception as e:
        print(f"Error drawing rectangle: {str(e)}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def add_text_to_rectangle_mac(x1: int, y1: int, x2: int, y2: int, text: str) -> dict:
    """Add text to a rectangle in Pages"""
    try:
        # Get screen size for coordinate scaling
        screen_width, screen_height = pyautogui.size()
        print(f"Screen size: {screen_width}x{screen_height}")
        
        # Calculate actual coordinates based on screen size
        def scale_coord(coord, max_val):
            return int((coord / 1000) * max_val)
        
        # Scale coordinates to screen size
        x1_scaled = scale_coord(x1, screen_width)
        y1_scaled = scale_coord(y1, screen_height)
        x2_scaled = scale_coord(x2, screen_width)
        y2_scaled = scale_coord(y2, screen_height)
        
        # Calculate center point for text
        center_x = (x1_scaled + x2_scaled) // 2
        center_y = (y1_scaled + y2_scaled) // 2
        print(f"Center point calculated: ({center_x}, {center_y})")
        
        script = f'''
        tell application "Pages"
            activate
            -- Create new document if none exists
            if not (exists document 1) then
                make new document
            end if
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

        print("Starting text creation...")
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=60)
        
        # Move mouse to initial position and click
        print(f"Moving to initial point: ({x1_scaled}, {y1_scaled})")
        pyautogui.moveTo(x1_scaled, y1_scaled, duration=0.2)        
        pyautogui.click()
        time.sleep(0.2)
        
        # Type the text
        pyautogui.write(text)
        time.sleep(0.2)

        # Select all text (Command + A)
        pyautogui.hotkey('command', 'a')
        time.sleep(0.2)
        pyautogui.hotkey('command', 'left')
        time.sleep(0.2)
        # Calculate number of space and enter presses needed
        # Each space moves text right, each enter moves text down
        x_spaces = (center_x - x1_scaled) // 10  # Move 5 pixels per space
        y_enters = (center_y - y1_scaled) // 20 # Move 5 pixels per enter

        print(f"Moving text to center using {x_spaces} spaces and {y_enters} enters")

        # Move vertically with enters
        for _ in range(y_enters):
            pyautogui.press('enter')
            time.sleep(0.01)
        # Move horizontally with spaces
        for _ in range(x_spaces):
            pyautogui.press('space')
            time.sleep(0.01)

        # Deselect text (Escape)
        pyautogui.press('esc')
        time.sleep(0.2)

        print("Text creation and positioning completed")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text created and moved to center position ({center_x}, {center_y}) with text '{text}'"
                )
            ]
        }
        
    except Exception as e:
        print(f"Error in add_text_to_rectangle_mac: {str(e)}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error creating text: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_pages_mac() -> dict:
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
