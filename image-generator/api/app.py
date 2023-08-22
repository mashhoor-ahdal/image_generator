import requests
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HEADERS = {"Authorization": "Bearer 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"}

def query_model(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content

@app.route("/", methods=["GET", "POST"])
def home():
    image_data = None
    if request.method == "POST":
        input_text = request.form["input_text"]

        image_bytes = query_model({"inputs": input_text})

        image_data = base64.b64encode(image_bytes).decode("utf-8")

    return render_template("index.html", image_data=image_data)

if __name__ == "__main__":
    app.run(debug=True)
