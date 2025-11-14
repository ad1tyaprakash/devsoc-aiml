from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
INPUT_FILE = "text.txt"
OUTPUT_FILE = "responses.json"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def read_file(fileinput) :
    with open(fileinput,"r") as f :
        return f.read()

def query(api_url,api_key,user_content) :
    headers = { "Authorization": f"Bearer {api_key}","Content-Type": "application/json" }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": "You are supposed to answer questions regarding AI"},{"role": "user", "content": user_content}]}
    response = requests.post(api_url, headers=headers, json=payload)
    try:
        return response.json()
    except Exception:
        return {"error": "Invalid JSON", "response_text": response.text}

def save_output(data, fileinput):
    with open(fileinput, "w") as f:
        json.dump(data, f, indent=2)

def main():
    user_content = read_file(INPUT_FILE)
    response = query(API_URL, API_KEY, user_content)
    save_output(response, OUTPUT_FILE)
    print(f"Response saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()