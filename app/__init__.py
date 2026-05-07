import os
import resend
from flask import Flask, render_template
from flask_compress import Compress
from config import config
from app.data.loader import load_all

compress = Compress()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    compress.init_app(app)
    app.config["SITE_DATA"] = load_all()

    resend.api_key = app.config["RESEND_API_KEY"]

    from app.routes import main
    app.register_blueprint(main)

    @app.errorhandler(404)
    def not_found(e):
        data = app.config["SITE_DATA"]
        return render_template("404.html", **data), 404

    return app
