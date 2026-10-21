from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import chat

app = Flask(__name__)
CORS(app)


@app.route("/api/weather_chat/", methods=["POST"])
def weather_chat():
    data = request.get_json()
    message = data.get("message", "")
    preferences = data.get("preferences", {})
    session_id = data.get("session_id", "default")

    if not message.strip():
        return jsonify({"error": "message 不可為空"}), 400

    reply = chat(session_id, message, preferences)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=8000)