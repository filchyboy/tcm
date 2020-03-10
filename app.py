from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Worldly Beings! I have arrived."

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()