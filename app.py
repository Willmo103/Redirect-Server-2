from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/maint", methods=["GET"])
def down_for_maintenance():
    return render_template(
        "template.jinja",
        title="Server Down",
        text="Server Down for Maintenance. Please check back later or contact the administrator.",
        img=url_for("static", filename="img/Maint.png"),
    )


@app.route("/404", methods=["GET"])
def page_not_found():
    return render_template(
        "template.jinja",
        title="Error 404",
        text="Error 404: Page Not Found",
        img=url_for("static", filename="img/404.png"),
    )


@app.route("/500", methods=["GET"])
def internal_server_error():
    return render_template(
        "template.jinja",
        title="Error 500",
        text="Error 500: Internal Server Error",
        img=url_for("static", filename="img/500.png"),
    )

@app.route("/message", methods=["GET"])
def message_and_redirect():
    return render_template(
        "template.jinja",
        title=get_title(),
        text=get_message,
        img=url_for("static", filename="img/500.png"),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9404)
