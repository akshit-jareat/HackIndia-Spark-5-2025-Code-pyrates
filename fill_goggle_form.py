import pyautogui
import time
import pygetwindow as gw
from user_data import User  # Assume you have a User class in another file or use data directly.

def bring_browser_to_foreground(window_title="Google Chrome - Google Form"):
    """Brings the browser window with the Google Form to the foreground."""
    try:
        # Find the window with the title containing Google Form (can be different based on your browser title)
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            # Focus the first window with the given title
            window = windows[0]
            window.activate()
            print(f"Focused on window: {window_title}")
        else:
            print(f"No window with the title '{window_title}' found.")
    except Exception as e:
        print(f"Error focusing on the window: {e}")

def fill_google_form(user_data):
    if user_data:
        print(f"Filling out the Google Form with the following data: {user_data.name}, {user_data.email}")

        # Focus on the Google Form window
        bring_browser_to_foreground("Google Chrome - Google Form")  # Modify this to match your browser window title

        # Wait for a few seconds to allow the browser window to become active
        time.sleep(3)

        # Coordinates of the form fields (Adjust these based on your form)
        name_field_coords = (500, 500)  # Replace with actual coordinates
        email_field_coords = (500, 600)  # Replace with actual coordinates
        address_field_coords = (500, 700)  # Replace with actual coordinates
        phone_field_coords = (500, 800)  # Replace with actual coordinates

        # Fill the name field
        pyautogui.moveTo(name_field_coords)
        pyautogui.click()
        pyautogui.write(user_data.name)

        # Fill the email field
        pyautogui.moveTo(email_field_coords)
        pyautogui.click()
        pyautogui.write(user_data.email)

        # Fill the address field
        pyautogui.moveTo(address_field_coords)
        pyautogui.click()
        pyautogui.write(user_data.address)

        # Fill the phone number field
        pyautogui.moveTo(phone_field_coords)
        pyautogui.click()
        pyautogui.write(user_data.phone)

        print("Google Form filled successfully!")
    else:
        print("No user data available to fill the form.")

if __name__ == "__main__":
    # Load stored user data (this can be modified to read from a database or file)
    user_data = User.get_user_data()
    fill_google_form(user_data)
