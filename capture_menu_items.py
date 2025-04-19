import pyautogui
import time

def capture_menu_items():
    print("This script will help capture the menu items we need.")
    print("Please follow these steps:")
    print("1. Make sure Pages is open")
    print("2. When ready, you'll have 5 seconds to:")
    print("   - Move your mouse over the Insert menu")
    
    input("Press Enter when ready to capture Insert menu...")
    print("Waiting 5 seconds...")
    time.sleep(5)
    
    # Capture Insert menu
    insert_region = pyautogui.screenshot('/Users/priye/Desktop/EAGV1/Session4/insert_menu.png')
    print("Captured Insert menu")
    
    print("\nNow:")
    print("1. Click the Insert menu")
    print("2. When ready, you'll have 5 seconds to:")
    print("   - Move your mouse over the Pen tool option")
    
    input("Press Enter when ready to capture Pen tool...")
    print("Waiting 5 seconds...")
    time.sleep(5)
    
    # Capture Pen tool
    pen_region = pyautogui.screenshot('/Users/priye/Desktop/EAGV1/Session4/pen_tool.png')
    print("Captured Pen tool")
    
    print("\nCapture complete! Created:")
    print("- insert_menu.png")
    print("- pen_tool.png")

if __name__ == "__main__":
    capture_menu_items() 