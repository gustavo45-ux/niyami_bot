from flask import Flask, render_template, redirect, request, session
import requests
import threading
from database import setup, connect
from bot.main import run_bot
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SECRET_KEY
import os

app = Flask(__name__)
app.secret_key = SECRET_KEY
API = "https://discord.com/api"

def get_user(token):
    return requests.get(f"{API}/users/@me", headers={"Authorization": f"Bearer {token}"}).json()

def get_guilds(token):
    return requests.get(f"{API}/users/@me/guilds", headers={"Authorization": f"Bearer {token}"}).json()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return redirect(f"{API}/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds")

@app.route("/callback")
def callback():
    code = request.args.get("code")
    data = {"client_id": CLIENT_ID,"client_secret": CLIENT_SECRET,"grant_type":"authorization_code","code":code,"redirect_uri":REDIRECT_URI}
    r = requests.post(f"{API}/oauth2/token", data=data, headers={"Content-Type":"application/x-www-form-urlencoded"})
    token = r.json().get("access_token")
    session["token"] = token
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "token" not in session:
        return redirect("/")
    guilds = get_guilds(session["token"])
    return render_template("dashboard.html", guilds=guilds)

@app.route("/guild/<int:guild_id>", methods=["GET","POST"])
def guild_settings(guild_id):
    conn = connect()
    c = conn.cursor()
    if request.method == "POST":
        counting = 1 if request.form.get("counting") else 0
        tickets = 1 if request.form.get("tickets") else 0
        events = 1 if request.form.get("events") else 0
        giveaways = 1 if request.form.get("giveaways") else 0
        c.execute("""INSERT OR REPLACE INTO guild_config
            (guild_id,counting_enabled,tickets_enabled,events_enabled,giveaways_enabled)
            VALUES (?,?,?,?,?)""",(guild_id,counting,tickets,events,giveaways))
        conn.commit()
    c.execute("SELECT * FROM guild_config WHERE guild_id=?",(guild_id,))
    config = c.fetchone()
    conn.close()
    return render_template("guild.html", guild_id=guild_id, config=config)


if __name__ == "__main__":
    setup()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


