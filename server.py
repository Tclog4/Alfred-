from flask import Flask, request, jsonify
from core.brain import AlfredBrain


app = Flask(__name__)

alfred = AlfredBrain()


@app.route("/")
def home():

    return "🤖 Alfred API is online"



@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data.get("message", "")


    response = alfred.think(message)


    return jsonify({
        "reply": response
    })



if __name__ == "__main__":

    print("🤖 Alfred API starting...")

    app.run(
        host="0.0.0.0",
        port=5000
    )
