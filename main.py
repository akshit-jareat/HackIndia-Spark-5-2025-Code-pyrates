from nlp_input import get_user_input
from llm_extractor import extract_user_data
from models import User
from filler import fill_form

def main():
    user_text = get_user_input()
    extracted_data = extract_user_data(user_text)

    user = User(
        name=extracted_data.get("name", ""),
        email=extracted_data.get("email", ""),
        address=extracted_data.get("address", ""),
        phone=extracted_data.get("phone", "")
    )

    user.save()
    fill_form(user)

if __name__ == "__main__":
    main()
