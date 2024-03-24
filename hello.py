from flask import Flask

app = Flask(__name__)

@app.route("/") # Decorator # home page url
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping",methods = ["GET"]) # home page/ping # Default method will be Get
def pinger():
    return "<H1>I am pinging!</H1>"