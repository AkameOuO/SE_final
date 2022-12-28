from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def main():
    return """<h1>逢甲大學圖書薦購系統</h1><a href="/se_final"><button>NID登入</button></a>"""

@app.route("/se_final")
def login():
    return redirect("https://judge.akameowo.ml/nid_login?forSe=1")

@app.route("/result")
def result():
    return "歡迎{type} {classname} {name}({id})！".format(**request.args)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)