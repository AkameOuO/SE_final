from random import randbytes
from datetime import timedelta
from flask import Flask, redirect, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = randbytes(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route("/")
def main():
    return """<h1>逢甲大學圖書薦購系統</h1><a href="/se_final"><button>NID登入</button></a>"""

@app.route("/se_final")
def login():
    return redirect("https://judge.akameowo.ml/nid_login?forSe=1")

@app.route("/result")
def result():
    session.update(request.args)
    return redirect("/welcome")

@app.route("/welcome")
def welcome():
    return "歡迎{type} {classname} {name}({id})！".format(**session)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)