from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please live your best life, like, and comment on this video, lets go. PS: I got a new job!!!'
