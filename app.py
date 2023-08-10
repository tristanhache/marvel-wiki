from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/iron-man")
def ironman():
    return render_template("iron-man.html")
