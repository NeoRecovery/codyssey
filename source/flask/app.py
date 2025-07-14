from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    # 서버 실행: 0.0.0.0:8080
    app.run(host="0.0.0.0", port=8080)