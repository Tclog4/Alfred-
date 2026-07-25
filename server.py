from flask import Flask, request, jsonify
from core.brain import AlfredBrain


app = Flask(__name__)

alfred = AlfredBrain()


@app.route("/")
def home():
    return "🤖 Alfred is online"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data.get("message", "")

    reply = alfred.think(message)

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":

    print("🤖 Alfred server started")

    app.run(
        host="0.0.0.0",
        port=5000
    )
