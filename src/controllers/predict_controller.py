from flask import request, jsonify, Blueprint
import numpy as np
from src.model.predict import test_pipeline

predicts = Blueprint("predicts", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@predicts.route("/", methods=["POST"])
def upload_file():
    return ''
    # try:
    #     if "file" not in request.files:
    #         raise ValueError("File not found in the request.")

    #     file = request.files["file"]

    #     if file.filename == "":
    #         raise ValueError("Empty filename in the request.")

    #     if file and allowed_file(file.filename):
    #         image = file.read()
    #         image_data = np.frombuffer(image, np.uint8)
    #         results = test_pipeline(image_data)
    #         return jsonify(results), 200
    #     else:
    #         raise ValueError("Invalid file type.")

    # except Exception as e:
    #     return f"Error processing file: {str(e)}", 500
