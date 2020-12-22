from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def hello_world():
    return "hello flask"

# python3 my_wsgi_server.py flask_app:flask_app
