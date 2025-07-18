from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello flask."

@app.route('/greeting/<name>')
def greet(name):
    return "Hello " + name
@app.route("/bye")
def say_bye():
    return "Bye!"
if __name__ == '__main__':
    app.run(debug=True)
