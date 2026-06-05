from flask import Blueprint
from flask import request
from flask import jsonify

import logging

from backend.services.security_service import analyze_code
from backend.security.validators import validate_code

security_bp = Blueprint(
    "security",
    __name__
)


@security_bp.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "JSON requerido"
            }), 400

        if "code" not in data:

            return jsonify({
                "error": "Campo code requerido"
            }), 400

        code = data["code"]

        if not validate_code(code):

            return jsonify({
                "error": "Código inválido"
            }), 400

        logging.info(
            "Solicitud de análisis recibida"
        )

        result = analyze_code(code)

        return jsonify(result), 200

    except Exception as e:

        logging.error(
            f"Error en predict: {str(e)}"
        )

        return jsonify({
            "error": "Error interno del servidor"
        }), 500