import os
from flask import Blueprint, render_template, current_app, jsonify

main = Blueprint("main", __name__)

_SLIDESHOW_DIR = os.path.join(os.path.dirname(__file__), "static", "assets", "slideshow")
_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def get_slideshow_images(directory=None):
    directory = directory or _SLIDESHOW_DIR
    if not os.path.isdir(directory):
        return []
    return sorted(
        f for f in os.listdir(directory)
        if os.path.splitext(f)[1].lower() in _IMAGE_EXTS
    )


@main.route("/")
def index():
    data = current_app.config["SITE_DATA"]
    return render_template("index.html", slideshow_images=get_slideshow_images(), **data)


@main.route("/resume")
def resume():
    data = current_app.config["SITE_DATA"]
    return render_template("resume.html", **data)


@main.route("/health")
def health():
    return jsonify({"status": "ok"})
