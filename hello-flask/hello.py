from flask import Flask

hello_flask = Flask(__name__)


@hello_flask.route("/")
def hello():
    return "Hello, World!"


@hello_flask.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    hello_flask.run(port=8080, debug=True)

