from flask import Blueprint
from src.controllers.predict_controller import predicts
from src.controllers.home_controller import home

api = Blueprint("api", __name__)
api.register_blueprint(predicts, url_prefix="/predicts")

web = Blueprint("web", __name__)
web.register_blueprint(home)
