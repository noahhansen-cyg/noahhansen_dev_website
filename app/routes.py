import os
import threading
import resend
from flask import Blueprint, render_template, current_app, jsonify, request

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


@main.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"error": "All fields are required."}), 400

    if current_app.config.get("RESEND_API_KEY"):
        from_addr = current_app.config["MAIL_FROM"]
        to_addr = current_app.config["MAIL_RECIPIENT"]
        app = current_app._get_current_object()

        def send_async():
            try:
                resend.Emails.send({
                    "from": from_addr,
                    "to": to_addr,
                    "reply_to": email,
                    "subject": f"Portfolio contact from {name}",
                    "text": f"Name: {name}\nEmail: {email}\n\n{message}",
                })
            except Exception:
                app.logger.exception("Failed to send contact email")

        threading.Thread(target=send_async, daemon=True).start()
    else:
        current_app.logger.info(
            "[DEV] Contact form: from=%s <%s> message=%s", name, email, message
        )

    return jsonify({"success": True})


@main.route("/health")
def health():
    return jsonify({"status": "ok"})
