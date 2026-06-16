import os
from flask import Flask, render_template, request, jsonify
from google import genai

MERI_API_KEY = os.environ.get("MERI_API_KEY")

client = genai.Client(api_key=MERI_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    sawaal = request.json.get("message")
    jawab = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=sawaal
    )
    return jsonify({"reply": jawab.text})

if __name__ == "__main__":
    app.run(debug=True)
