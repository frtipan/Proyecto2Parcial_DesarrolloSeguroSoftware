import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from flask import Flask
from flask import request
from flask import jsonify

from src.ml.predict import predict_code

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "status": "running",
        "service": "AI Security Scanner"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "No JSON recibido"
        }), 400

    if "code" not in data:

        return jsonify({
            "error": "Debe enviar el campo 'code'"
        }), 400

    code = data["code"]

    result = predict_code(code)

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )