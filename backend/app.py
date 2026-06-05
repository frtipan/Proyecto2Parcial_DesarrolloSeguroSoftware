from flask import Flask

from flask_talisman import Talisman

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from backend.controllers.security_controller import security_bp

app = Flask(__name__)

Talisman(
    app,
    force_https=False
)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per minute"]
)

app.register_blueprint(
    security_bp
)


@app.route("/")
def home():

    return {
        "message": "Secure Code Detector API.",
        "status": "running"
    }


@app.route("/health")
def health():

    return {
        "status": "ok"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )