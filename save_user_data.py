from models import User

def save_user_data(name, email, address, phone):
    user = User(name, email, address, phone)
    user.save()

if __name__ == "__main__":
    save_user_data('John Doe', 'john@example.com', '1234 Elm St.', '555-1234')
