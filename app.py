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
    return render_template("movies/marvel/phase1/iron-man.html")

@app.route("/incredible-hulk")
def incrediblehulk():
    return render_template("movies/marvel/phase1/incredible-hulk.html")

@app.route("/iron-man-2")
def ironman2():
    return render_template("movies/marvel/phase1/iron-man-2.html")

@app.route("/thor")
def thor():
    return render_template("movies/marvel/phase1/thor.html")

@app.route("/captain-america-first-avengers")
def capamericafirstavengers():
    return render_template("movies/marvel/phase1/captain-america-first-avengers.html")

@app.route("/the-avengers")
def theavengers():
    return render_template("movies/marvel/phase1/the-avengers.html")



@app.route("/iron-man-3")
def ironman3():
    return render_template("movies/marvel/phase2/iron-man-3.html")

@app.route("/thor-dark-world")
def thordarkworld():
    return render_template("movies/marvel/phase2/thor-dark-world.html")

@app.route("/captain-america-winter-soldier")
def capamericawintersoldier():
    return render_template("movies/marvel/phase2/captain-america-winter-soldier.html")

@app.route("/guardian-of-the-galaxy")
def gotg():
    return render_template("movies/marvel/phase2/guardian-of-the-galaxy.html")

@app.route("/avengers-age-ultron")
def ageultron():
    return render_template("movies/marvel/phase2/avengers-age-ultron.html")

@app.route("/ant-man")
def antman():
    return render_template("movies/marvel/phase2/ant-man.html")