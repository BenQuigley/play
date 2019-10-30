import os

import jinja2

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/change")
def chance():
    return redirect("/")


@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        return render_template("post.html")
    return render_template("get.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
