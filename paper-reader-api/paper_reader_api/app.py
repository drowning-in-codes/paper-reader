from flask import Flask
app = Flask(__name__)

@app.route("/paper/<string:topic>")
def get_papers(topic):




    return "<p>Hello, World!</p>"