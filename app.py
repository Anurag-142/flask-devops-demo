from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🚀 Flask DevOps Demo</h1>
    <p>Welcome to Project 2.</p>
    <p>This application is running successfully.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)