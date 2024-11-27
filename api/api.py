from flask import Flask
from flask_restful import Api
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

from endpoints.boardgame import Boardgame
from endpoints.health import Health
from config import Config

def build_app():
    app = Flask(__name__)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    api = Api(app)
    api.add_resource(Health, "/health", endpoint="health")
    api.add_resource(Boardgame, "/boardgame", endpoint="boardgame")

    return app

if __name__ == '__main__':
    config = Config()
    
    app = build_app()
    app.run(
        host=config.APP_HOST,
        port=config.APP_PORT,
        debug=config.APP_DEBUG
    )
