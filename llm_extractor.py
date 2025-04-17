# llm_extractor.py

from transformers import pipeline
from dotenv import load_dotenv
import os
import json

# Load your .env variables
load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")

# Use Hugging Face's pipeline with a hosted model
pipe = pipeline("text2text-generation", 
                model="declare-lab/flan-alpaca-large", 
                token=HF_TOKEN)

def extract_user_data(text):
    prompt = (
        f"Extract the following information from the text:\n"
        f"Name, Email, Address, Phone Number\n\n"
        f"Text: {text}\n\n"
        f"Respond in JSON format like:\n"
        f"{{\"name\": \"\", \"email\": \"\", \"address\": \"\", \"phone\": \"\"}}"
    )

    response = pipe(prompt, max_new_tokens=100)[0]['generated_text']

    # Try to fix formatting if needed
    try:
        # Ensure the response is wrapped in curly braces
        formatted_response = "{" + response.strip().strip(",") + "}"
        json_data = json.loads(formatted_response)
        return json_data
    except Exception as e:
        print("❌ Error parsing response:", e)
        print("📦 Raw LLM response:", response)
        return None
