from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home<h1/>"

@app.route("/login")
def login():
    return "<h1>LogIn<h1/>"

@app.route("/logout")
def logout():
    return render_template('logout.html')


if __name__ == "__main__":
    app.run(debug=True)

