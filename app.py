from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_cors import CORS
from data import DataManager
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for the session
CORS(app, resources={r"/api/*": {"origins": "*"}})
data = DataManager.from_file() if os.path.exists(DataManager.JSON_PATH) else DataManager()

modify_secret_key_hash = generate_password_hash(os.environ.get('MODIFY_SECRET_KEY'))

@app.route("/", methods=["GET"])
def index():
    return redirect("/message")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        if check_password_hash(modify_secret_key_hash, password):
            session['logged_in'] = True
            return redirect("/admin")
        else:
            return "Invalid password", 403
    return render_template("login.jinja.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('logged_in'):
        return redirect("/login")

    if request.method == "POST":
        updated_data = {}
        for key, value in request.form.items():
            if value:
                updated_data[key] = value
        data.update_fields(**updated_data)
        return redirect("/admin")

    return render_template("admin.jinja.html", title="Data Manager", data=data.serialize())



@app.route("/maint", methods=["GET"])
def down_for_maintenance():
    return render_template(
        "template.jinja.html",
        title="Server Down",
        text="Server Down for Maintenance. Please check back later or contact the administrator.",
        img=url_for("static", filename="img/Maint.png"),
    )


@app.route("/404", methods=["GET"])
def page_not_found():
    return render_template(
        "template.jinja.html",
        title="Error 404",
        text="Error 404: Page Not Found",
        img=url_for("static", filename="img/404.png"),
    )


@app.route("/500", methods=["GET"])
def internal_server_error():
    return render_template(
        "template.jinja.html",
        title="Error 500",
        text="Error 500: Internal Server Error",
        img=url_for("static", filename="img/500.png"),
    )


@app.route("/message", methods=["GET"])
def message_and_redirect():
    return render_template(
        "message_forward.jinja.html",
        title="README",
        text=data.message,
        date=data.date,
        redirect=data.redirect,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9404, debug=True)
