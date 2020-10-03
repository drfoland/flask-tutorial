from utility_functions import *

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/test")
def test():
    return "Flask is up and running.", 200
    
@app.route("/")
def home():
    global data
    data['count'] += 1
    write_data(data)
    return render_template("index.html", counter=data['count'])

if __name__ == "__main__":
    app.run(debug=True, port=5000)