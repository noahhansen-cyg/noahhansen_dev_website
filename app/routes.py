from flask import Blueprint, render_template, current_app, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def index():
    data = current_app.config["SITE_DATA"]
    return render_template("index.html", **data)


@main.route("/resume")
def resume():
    data = current_app.config["SITE_DATA"]
    return render_template("resume.html", **data)


@main.route("/health")
def health():
    return jsonify({"status": "ok"})
