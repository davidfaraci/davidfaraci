from flask import Flask, render_template, send_from_directory
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path='')
auth = HTTPBasicAuth()
Mobility(app)

users = {}
fileloc = 'login'
with open(fileloc) as i:
     for line in i:
          (key, val) = line.split()
          users[key] = val

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/research")
def pubs():
    return render_template('research.html')

@app.route("/teaching")
def teach():
    return render_template('teaching.html')

@app.route("/opentower")
def ot():
    return render_template('opentower.html')

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

@auth.get_password #password protection for private storage directory
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/private/<path:path>') #URL handler for private storage directory
@auth.login_required
def private(path):
    return send_from_directory('private', path)
