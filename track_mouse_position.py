import pyautogui
import time

print("Move your mouse to the form field you want to track and press 'CTRL+C' to stop the script.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse Position: X={x} Y={y}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nMouse tracking stopped.")
