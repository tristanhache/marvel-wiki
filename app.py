from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
    
@app.route("/iron-man")
def ironman():
    return render_template("movies/marvel/iron-man/iron-man.html")
