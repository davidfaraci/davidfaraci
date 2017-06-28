from flask import Flask, render_template, send_from_directory
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template


app = Flask(__name__, static_url_path='')

Mobility(app)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/publications")
def pubs():
    return render_template('publications.html')

@app.route("/wip")
def wip():
    return render_template('wip.html')

@app.route("/opentower")
def ot():
    return render_template('opentower.html')

@app.route("/teaching")
def teach():
    return render_template('teaching.html')

@app.route("/misc")
def misc():
    return render_template('misc.html')

@app.route('/MD')
def MD():
    return render_template('MD.html')

@app.route('/cryptic')
def cryptic():
    return render_template('cryptic.html')

@app.route('/workshop')
def workshop():
    return render_template('workshop.html')

@app.route('/<path:filename>')
def storage(filename):
    return send_from_directory('static', filename)
