from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Simple keyword-based responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! Need any assistance?",
        "how are you": "I'm just code, but I'm doing great! Thanks for asking.",
        "what is your name": "I'm your friendly chatbot!",
        "bye": "Goodbye! Have a nice day!",
        "thank you": "You're welcome!",
        "who made you": "I was created by Ashwini Sharma 😊",
        "what can you do": "I can answer simple questions. Try asking me something!",
    }

    # Find a matching response or default
    bot_response = responses.get(user_message, "I'm not sure how to answer that. Try asking something else.")

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
