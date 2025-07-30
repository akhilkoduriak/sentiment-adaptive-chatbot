from flask import Flask, request, render_template, jsonify
from textblob import TextBlob


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower().strip()

    if not user_message:
        return jsonify({"reply": "Please say something!"})

    analysis = TextBlob(user_message)
    polarity = analysis.sentiment.polarity

    # Keyword-based responses first
    if "python" in user_message:
        bot_reply = "Python is a versatile language! Are you into data science, automation, or web development?"
    elif "ai" in user_message or "machine learning" in user_message:
        bot_reply = "AI is a powerful tool. Are you working on any AI projects?"
    elif "hello" in user_message or "hi" in user_message or "hey" in user_message:
        bot_reply = "Hi there! How can I assist you today?"
    elif "thank" in user_message:
        bot_reply = "You're welcome! Let me know if there's anything else I can help with."

    # Sentiment-based fallback responses
    elif polarity > 0.2:
        bot_reply = "That's wonderful to hear! 😊 How else can I help?"
    elif polarity < -0.2:
        bot_reply = "I'm sorry you're feeling that way. Want to talk about it?"
    else:
        bot_reply = "I see. What would you like to discuss?"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
