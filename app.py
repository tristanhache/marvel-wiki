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
    return render_template("movies/marvel/iron-man.html")

@app.route("/incredible-hulk")
def incrediblehulk():
    return render_template("movies/marvel/incredible-hulk.html")

@app.route("/iron-man-2")
def ironman2():
    return render_template("movies/marvel/iron-man-2.html")

@app.route("/thor")
def thor():
    return render_template("movies/marvel/thor.html")

@app.route("/captain-america-first-avengers")
def capamericafirstavengers():
    return render_template("movies/marvel/captain-america-first-avengers.html")

@app.route("/the-avengers")
def theavengers():
    return render_template("movies/marvel/the-avengers.html")