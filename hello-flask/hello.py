from flask import Flask

hello_flask = Flask(__name__)


@hello_flask.route("/")
def hello():
    return "Hello, World!"


@hello_flask.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    """
     In case you dockerized the app, you should give host as '0.0.0.0'
     since Flask is binding to localhost (127.0.0.1) and that will only
     be reachable from within the container, see the link below for more info.
     https://devops.stackexchange.com/questions/3380/dockerized-flask-connection-reset-by-peer
    """
    hello_flask.run(host="0.0.0.0", port=5000, debug=True)

