from flask import Flask

hello_flask = Flask(__name__)


@hello_flask.route("/")
def hello():
    return "Hello, World!"


@hello_flask.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    hello_flask.run(host="0.0.0.0", port=5000, debug=True)

