from flask import Flask, render_template, request, jsonify
from google import genai

MERI_API_KEY = "APNI_KEY_YAHAN_DAALO"

client = genai.Client(api_key=MERI_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    sawaal = request.json.get("message")
    jawab = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=sawaal
    )
    return jsonify({"reply": jawab.text})

if __name__ == "__main__":
    app.run(debug=True)