from flask import Flask
def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key='123456789' #securely send messages back and forth from the user

    from . import urlshort
    app.register_blueprint(urlshort.bp)


    return app