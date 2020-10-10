from utility_functions import *

import os

from flask import Flask
from flask import render_template
from flask import url_for
from flask import send_from_directory
from flask import request
#from flask import make_response

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/test")
def test():
    return "Flask is up and running.", 200
    
@app.route("/")
def home():
    data = read_data("general")
    data['count'] += 1
    write_data(data, "general")
    return render_template("index.html", counter=data['count'])
    
@app.route("/login")
def login():
    # TODO
    return "login", 200
    
@app.route("/create", methods=['get'])
def create_get():
    return render_template("create-account.html")
    
@app.route("/create", methods=['post'])
def create_post():
    print(f"Username: {request.form['username']}")
    print(f"Password: {request.form['password']}")
    users = read_data("users")
    if request.form['username'] not in users.keys():
        users[request.form['username']] = {"password": request.form['password']}
        write_data(users, "users")
        return "", 201
    else:
        return "", 409
    
#@app.route('/set-cookie')
#def set_cookie():
#    res = make_response()
#    res.set_cookie("name", value="I am cookie")
#    return res 

if __name__ == "__main__":
    app.run(debug=True, port=5000)