from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import joblib
import numpy as np
import os
import re
from dotenv import load_dotenv
import os

load_dotenv('env/secrets.env')
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

client = OpenAI(api_key=os.getenv('API_KEY'))
model = joblib.load("spam_classifier.pkl")

@app.route("/")
def home():
    return render_template("index.html")

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    email_text = data["email"]

    cleaned = clean_text(email_text)

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=cleaned
    )

    embedding = np.array(response.data[0].embedding).reshape(1, -1)
    pred = model.predict(embedding)[0]

    label = "Spam" if pred == 1 else "Ham"

    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(debug=True)
