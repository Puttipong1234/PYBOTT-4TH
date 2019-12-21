from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home Page"

@app.route("/uncle")
def uncle():
    return "This is uncle"

if __name__ == "__main__":
    app.run()