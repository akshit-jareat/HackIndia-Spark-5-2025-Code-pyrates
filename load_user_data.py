import json

def load_user_data():
    """Loads user data from the JSON file."""
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    except FileNotFoundError:
        print("No saved data found.")
        return None

# Example usage
user_data = load_user_data()
if user_data:
    print(user_data)
