from flask import Flask
from flask_cors import CORS
from src.router.routes import api, web

app = Flask(__name__, template_folder="./src/templates")
app.secret_key = "oOUP0oHOQKHnmZHbXT8IxQ99Ml4Q2ZMv"
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(web)

def create_app():
    return app