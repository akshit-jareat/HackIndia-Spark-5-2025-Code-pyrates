import json

class User:
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    def save(self):
        user_data = {
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone
        }
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)
        print("✅ User data saved.")

    @staticmethod
    def load():
        try:
            with open('user_data.json', 'r') as f:
                data = json.load(f)
            return User(**data)
        except FileNotFoundError:
            print("❌ No user data file found.")
            return None
