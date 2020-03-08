from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Worldly Beings! I have arrived."

if __name__ == '__main__':
    app.run()