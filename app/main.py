from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    with open('./static/index.html', 'r') as file:
        return file.read()

@app.route("/main.js")
def js():
    with open('./static/main.js', 'r') as file:
        return file.read()


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
