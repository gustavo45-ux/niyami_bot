from flask import Flask, render_template, request, redirect, url_for
import threading
from main import run_bot
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# -------- Routes panel --------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/giveaways")
def giveaways():
    return render_template("giveaways.html")

@app.route("/tickets")
def tickets():
    return render_template("tickets.html")

@app.route("/counting")
def counting():
    return render_template("counting.html")

# -------- Lancer le bot en thread --------
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
