from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# Create table for chat history
def init_db():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"reply": "❌ Empty message"}), 400

    # Save user message
    save_to_history("user", user_input)

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Always respond in well-formatted Markdown including lists, headings, and code blocks when necessary."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(GROQ_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        reply = response.json()["choices"][0]["message"]["content"]
        save_to_history("assistant", reply)
        return jsonify({"reply": reply})
    except requests.exceptions.RequestException as e:
        return jsonify({"reply": f"❌ API Error: {str(e)}"}), 500

def save_to_history(role, message):
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, message, timestamp) VALUES (?, ?, ?)", 
                   (role, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True) 