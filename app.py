from flask import Flask, render_template, request, url_for, redirect, jsonify
from data import DataManager

app = Flask(__name__)
data = DataManager.load_from_file()


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
        text=data.get_message(),
        date=data.get_date(),
    )


@app.route("/api/v1/data", methods=["GET"])
def api_message():
    return jsonify(data.serialize())


@app.route("/api/v1/data", methods=["POST"])
def api_update():
    if request.headers.get("X-Modify-Key") != data.MODIFY_SECRET_KEY:
        return jsonify({"error": "Invalid key"}), 403
    data.update_message(request.json.get("message"))
    return jsonify(data.serialize())


@app.route("/api/v1/data_schema", methods=["GET"])
def api_schema():
    schema = [key for key in data.serialize().keys()]
    return jsonify(schema)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9404)
