# LLM-Based power Form Filler

## Description
LLM-Based Form Filler is a Python tool that extracts personal details from natural language using a Hugging Face LLM and fills online forms automatically using PyAutoGUI. It streamlines repetitive form-filling by turning simple user input like "My name is Ali..." into structured form data.

## Features
- Accepts natural language input to extract structured user data
- Uses a Hugging Face-hosted LLM via API
- Auto-fills browser-based forms using PyAutoGUI
- Saves user profile data for reuse

## Folder Structure
```
form_filler_backend/
│
├── main.py               # Entry point of the application
├── llm_extractor.py      # Handles LLM API interaction and data extraction
├── models.py             # User data model
├── save_user_data.py     # Save/load user data to JSON
├── .env                  # Stores Hugging Face API token
├── user_data.json        # JSON file to store user profile data
└── README.md             # Project documentation
```

## Requirements
- Python 3.8+
- PyAutoGUI
- Transformers
- Hugging Face Hub
- Torch (PyTorch)
- python-dotenv

## Setup Instructions
1. **Clone the repository**
```bash
git clone https://github.com/akshit-jareat/HackIndia-Spark-5-2025-Code-pyrates
cd HackIndia-Spark-5-2025-Code-pyrates
```

2. **Create and activate virtual environment (optional but recommended)**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your Hugging Face API token to `.env`**
```
HUGGINGFACEHUB_API_TOKEN=YOUR_SECRET_TOKEN
```
HOW TO ACCESS THIS 
  1. CREATE .env file in your root directory
  2. inside .env , add this line of 4th point 

5. **Run the app**
```bash
python main.py
```

## How It Works
- Takes your details in natural language
- Sends the text to the Hugging Face LLM for extraction
- Extracted data is stored and used to auto-fill browser forms via PyAutoGUI

## Example Input
```
My name is Hina, email is hina@gmail.com, I live in Karachi, and my phone number is 03451234567.
```

## Disclaimer
This tool uses screen automation (PyAutoGUI). Make sure the browser form is open and the first input field is focused when you run the script.



