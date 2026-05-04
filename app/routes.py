import os
from flask import Blueprint, render_template, current_app, jsonify

main = Blueprint("main", __name__)

_PHOTOS_DIR = os.path.join(os.path.dirname(__file__), "static", "assets", "photos")
_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def get_photos(directory=None):
    directory = directory or _PHOTOS_DIR
    if not os.path.isdir(directory):
        return []
    return sorted(
        f for f in os.listdir(directory)
        if os.path.splitext(f)[1].lower() in _IMAGE_EXTS
    )


@main.route("/")
def index():
    data = current_app.config["SITE_DATA"]
    return render_template("index.html", photos=get_photos(), **data)


@main.route("/resume")
def resume():
    data = current_app.config["SITE_DATA"]
    return render_template("resume.html", **data)


@main.route("/health")
def health():
    return jsonify({"status": "ok"})
