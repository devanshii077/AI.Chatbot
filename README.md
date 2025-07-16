# 💬 AI Chatbot App

A simple, smart, and stylish Python-based chatbot that responds to user queries using predefined intents or basic NLP techniques.

Perfect for beginners, portfolios, or demo presentations! 🚀

---

## ✨ Features

🤖 Rule-based or ML-based intent recognition  
🎤 Voice input support (using SpeechRecognition)  
💬 Scrollable chat history  
🧠 Basic user memory (e.g., remembers your name)  
🌙 Dark/Light mode toggle  
📜 Button suggestions for quick replies  
💾 Auto-save chat logs to `.txt`  
💄 Clean modern UI with emojis, glowing buttons, and animations  

---

## 🛠️ Built With

- Python  
- Tkinter / CustomTkinter  
- NLTK / Scikit-learn (for ML-based classification)  
- SpeechRecognition + PyAudio (for microphone input)  
- JSON (for defining intents and responses)

---

## 📁 Folder Structure

AI.Chatbot/
│
├── chatbot/
│ ├── intents.json # List of chatbot intents and responses
│ ├── train.py # Script to train ML model (if used)
│ ├── model.pkl # Trained model (optional for ML-based bot)
│ └── chatbot.py # Core chatbot logic
│
├── ui/
│ └── app.py # Main GUI interface
│
├── assets/
│ └── logo.png # (Optional) UI assets
├── requirements.txt
└── README.md


## 🚀 How to Run

```bash
git clone https://github.com/devanshii077/AI.Chatbot.git
cd AI.Chatbot
pip install -r requirements.txt
python ui/app.py
