import os
from flask import Flask, jsonify
from config import config
from app.data.loader import load_all


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config["SITE_DATA"] = load_all()

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app
