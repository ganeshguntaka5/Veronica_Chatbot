

# 🤖 **AI Chatbot with Voice Interface**

<div align="center">

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-3.1.0-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Groq](https://img.shields.io/badge/Groq-API-orange)

</div>

A sleek, modern Flask-based web app featuring an AI-powered chatbot with a **voice interface**. Powered by the **Groq API**, this project blends natural language understanding and speech synthesis for a smart, accessible, and conversational user experience.

---

## ✨ **Features**

- 🤖 **AI-Powered Chat**  
  Smart responses generated using **Groq's LLaMA 3 model**

- 🎤 **Voice Interface**  
  - **Voice Input** (microphone support)  
  - **Text-to-Speech Output**  
  - **Switchable voice options** (male/female)

- 🌓 **Theme Support**  
  - Toggle between **Light** and **Dark** modes  
  - Fully **responsive UI** for all devices

- 💾 **Data Management**  
  - Persistent **chat history**  
  - Integrated with **SQLite** for storage

- 🔒 **Security First**  
  - API keys managed via **environment variables**  
  - API key never exposed in codebase  

---

## 🚀 **Quick Start**

### 🛠️ Prerequisites

- Python 3.8 or higher  
- A modern browser that supports **Web Speech API**  
- Groq API Key

---

### 📦 Installation

1. **Clone the Repository**
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. **Set Up Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Environment File**
```env
# .env file in root directory
GROQ_API_KEY=your_api_key_here
```

---

### ▶️ Running the App

```bash
python app.py
```

Then visit:  
👉 **http://localhost:5000**

---

## 🎮 **Usage Guide**

### 💬 Chat Interface

- Type messages into the input box  
- Hit **Enter** or click **Send**  
- Chat history will appear above

### 🔊 Voice Controls

- 🎤 Click the **microphone icon** to speak  
- 🔈 Use the **speaker icon** to enable/disable voice output  
- 👤 Switch between **male/female voice options**

### 🌓 Theme Switching

- Toggle between **Dark** and **Light** themes using the theme icon

---

## 📁 **Project Structure**

```
.
├── app.py              # Main Flask app
├── requirements.txt    # Dependencies
├── .env                # API keys and environment config
├── .gitignore          # Git ignored files
├── templates/
│   └── index.html      # Main UI template
└── chat_history.db     # SQLite DB for chat history
```

---

## 🔐 **Security Considerations**

- 🔑 API keys are securely stored in `.env`  
- 🚫 `.env` is excluded from Git using `.gitignore`  
- ✅ Input is validated and sanitized  
- ⚠️ Sensitive data never exposed in frontend

---

## 🤝 **Contributing**

We love contributions!  
Follow these steps to contribute:

1. Fork the repo  
2. Create a feature branch  
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes  
```bash
git commit -m "Add AmazingFeature"
```
4. Push and open a Pull Request  
```bash
git push origin feature/AmazingFeature
```

---

## 📝 **License**

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

---

## 🙏 **Acknowledgments**

- [Groq](https://groq.com/) — for blazing fast AI capabilities  
- [Flask](https://flask.palletsprojects.com/) — our lightweight backend hero  
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) — making voice interaction easy

---

## 📞 **Support**

For bugs, feature requests, or questions:  
👉 Open an issue on the GitHub repo or contact the maintainers directly.

---

<div align="center">

Made with ❤️ using Python, Flask, and AI magic ✨

</div>



# Veronica_Chatbot
🤖 AI Chatbot with Voice Interface - A Flask web app featuring Groq-powered chat, voice input/output, and theme support. Combines natural language processing with speech synthesis for an interactive chat experience. #Python #Flask #AI #VoiceInterface


