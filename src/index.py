import json
import subprocess

from flask import Flask, jsonify, render_template

app = Flask(__name__)


def get_pip_freeze():
    res = subprocess.run(
        "pip freeze", shell=True, stdout=subprocess.PIPE, encoding="utf-8"
    )
    pip_list = res.stdout.splitlines()
    return pip_list


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_pip")
def get_pip():
    pip_list = get_pip_freeze()
    return render_template("get_pip.html", pip_list=pip_list)


@app.route("/get_pip_ajax", methods=["POST"])
def get_pip_ajax():
    pip_list = get_pip_freeze()
    return jsonify(pip_list)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
