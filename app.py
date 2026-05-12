from flask import Flask, render_template, request
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine!", "Doing great!", "Awesome!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "your name": ["I am an AI Chatbot."],
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand."

@app.route("/", methods=["GET", "POST"])
def home():
    bot_reply = ""

    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = chatbot_response(user_message)

    return render_template("index.html", reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
