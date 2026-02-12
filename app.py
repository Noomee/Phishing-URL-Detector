from flask import Flask, render_template, request
from model import predict_url
import os  # Required for dynamic port in Render

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        result = predict_url(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    # Get port from environment (Render assigns dynamically)
    port = int(os.environ.get("PORT", 5000))
    # Host 0.0.0.0 required for Render to make app accessible externally
    app.run(host="0.0.0.0", port=port)

