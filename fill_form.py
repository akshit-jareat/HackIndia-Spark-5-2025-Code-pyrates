# fill_form.py

import pyautogui
import time

def fill_form():
    # Coordinates obtained from locate_mouse.py (example)
    name_field_coords = (500, 500)
    email_field_coords = (500, 600)
    
    # Move to the name field and click
    pyautogui.moveTo(name_field_coords)
    pyautogui.click()
    pyautogui.write("John Doe")

    # Move to the email field and click
    pyautogui.moveTo(email_field_coords)
    pyautogui.click()
    pyautogui.write("john@example.com")

    print("Form filled successfully!")

if __name__ == "__main__":
    fill_form()
