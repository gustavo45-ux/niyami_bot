from flask import Flask, render_template
import threading
import os
from bot.main import run_bot

# -------- Flask --------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # doit être défini dans Render

# -------- Routes --------
@app.route("/")
def home():
    return render_template("index.html")

# -------- Lancer le bot en thread --------
threading.Thread(target=run_bot, daemon=True).start()

# -------- Lancer Flask --------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
