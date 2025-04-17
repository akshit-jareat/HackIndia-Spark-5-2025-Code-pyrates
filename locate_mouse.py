import pyautogui
import time

print("Move your mouse to the form fields. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse Position: X={x}, Y={y}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped.")
