from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Word!"

@app.route("/paralalel")
def paralel():
    return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

if __name__ == "__main__" :
    app.run(debug=True)