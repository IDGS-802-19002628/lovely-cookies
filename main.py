from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola mundo</h1>"
@app.route("/login")
def login():
    return "<h1>Login</h1>"

if __name__ == "__main__":
    app.run(debug=True)