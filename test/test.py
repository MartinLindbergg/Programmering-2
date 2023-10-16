from flask import Flask, render_template

app = Flask(__name__)


page = """
    <html>
    <head><title>Hem</title></head>
    <body>
    <h1>Titel</h1>
    <p>Detta är Hem<p>
    </body>
    </html>
"""


@app.route("/")
def home():
    return page

@app.route("/login")
def login():
    return "<h1>LogIn<h1/>"

@app.route("/logout")
def logout():
    return render_template(logout.html)



if __name__ == "__main__":
    app.run(debug=True)

