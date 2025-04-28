from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is Running!"

def run_server():
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)