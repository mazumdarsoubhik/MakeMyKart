from flask import Flask, render_template, request
from model import LLM

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template('index.html', url="https://via.placeholder.com/400", headline="User Preference")