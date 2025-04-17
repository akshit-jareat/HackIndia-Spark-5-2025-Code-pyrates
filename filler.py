# filler.py

import pyautogui
import time
import pygetwindow as gw
from models import User
import mouse  # New import to detect mouse click


def bring_browser_to_foreground(title="Google Forms"):
    try:
        windows = gw.getWindowsWithTitle(title)
        if windows:
            windows[0].activate()
            print(f"✅ Browser window '{title}' focused.")
        else:
            print("❌ Could not find the browser window.")
    except Exception as e:
        print(f"❌ Error bringing window forward: {e}")


def wait_for_user_click():
    print("🖱️ Waiting for you to click on the first field...")
    while True:
        if mouse.is_pressed(button='left'):
            print("✅ Click detected. Starting to fill form...")
            break
        time.sleep(0.1)


def fill_form(user_data):
    if not user_data:
        print("❌ No data to fill.")
        return

    bring_browser_to_foreground("Google Forms")  # Adjust if needed

    wait_for_user_click()

    pyautogui.write(user_data.name)
    pyautogui.press('tab')
    pyautogui.write(user_data.email)
    pyautogui.press('tab')
    pyautogui.write(user_data.address)
    pyautogui.press('tab')
    pyautogui.write(user_data.phone)
    pyautogui.press('tab')

    print("✅ Form filled successfully!")
