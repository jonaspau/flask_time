from flask import Flask, render_template, request
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now(timezone("Europe/Oslo"))
    return render_template("index.html", now=now)
