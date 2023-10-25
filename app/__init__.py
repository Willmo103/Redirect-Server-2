from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/maint", methods=["GET"])
def down_for_maintenance():
    return render_template(
        "template.jinja",
        title="Server Down for Maintenance",
        img=url_for("static", filename="img/Maint.png"),
    )


@app.route("/404", methods=["GET"])
def page_not_found():
    return render_template(
        "template.jinja",
        title="Couldn't Find That Shit!",
        img=url_for("static", filename="img/404.png"),
    )


@app.route("/500", methods=["GET"])
def internal_server_error():
    return render_template(
        "template.jinja",
        title="Something Fucked Up!",
        img=url_for("static", filename="img/500.png"),
    )
