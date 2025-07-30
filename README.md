Sentiment-Adaptive Chatbot

Project Overview

This repository contains the source code and report for the project titled "Sentiment-Adaptive Chatbot: An AI-Powered Interface for Dynamic User Interaction". The chatbot is a web-based conversational interface that dynamically adapts its responses using AI-based sentiment analysis.

Features

🔍 Real-time sentiment analysis using TextBlob

💬 Keyword recognition for context-aware responses (e.g., Python, AI, greetings)

🤖 Adaptive responses: empathetic, neutral, or encouraging based on sentiment

🌐 Simple, responsive web interface with HTML/CSS/JavaScript

⚙️ Backend built using Python Flask

Installation & Setup

Prerequisites

Python 3.7+

pip (Python package manager)

Clone the Repository

git clone https://github.com/yourusername/sentiment-adaptive-chatbot.git
cd sentiment-adaptive-chatbot

Install Required Libraries

pip install -r requirements.txt
python -m textblob.download_corpora

Run the Application

python app.py

Open your browser and navigate to http://127.0.0.1:5000 to interact with the chatbot.

File Structure

sentiment-adaptive-chatbot/
├── app.py                 # Flask backend
├── requirements.txt       # Required Python packages
├── templates/
│   └── index.html         # Frontend interface
├── static/
│   └── style.css          # Custom CSS styling
└── README.md              # This file

How It Works

User sends a message via the browser interface.

Flask receives the message and analyzes it using TextBlob.

The polarity score determines if the sentiment is positive, neutral, or negative.

If any known keywords are detected, the bot prioritizes those topics in its reply.

The bot sends a tailored response back to the UI.

Sample Code (from app.py)

analysis = TextBlob(user_message)
polarity = analysis.sentiment.polarity

Sample Interactions

User: "Hi"
Bot: "Hi there! How can I assist you today?"

User: "I feel awesome."
Bot: "That's wonderful to hear! 😊 How else can I help?"

User: "I'm feeling very low."
Bot: "I'm sorry you're feeling that way. Want to talk about it?"

User: "Can you explain Python?"
Bot: "Python is a versatile language! Are you into data science, automation, or web development?"

Author

Sivarama Krishna Akhil Koduri

License

This project is for educational purposes only. No commercial license is granted.

Report

The full academic report (APA format) describing the architecture, implementation, challenges, and benefits of the chatbot can be found in the file:
Sentiment Chatbot Report.docx

Acknowledgments

TextBlob – Sentiment Analysis

Flask – Web Framework

University of the Cumberlands – Project Guidelines

GitHub Repository

