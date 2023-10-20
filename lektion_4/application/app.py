from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    '''Plats för kommentarer'''
    #Koden kommer hamna här
    return render_template('index.html')


@app.route("/form")
def form():
    '''Plats för kommentar'''
    return render_template('form.html')


@app.post("/api")
def api_post():
    '''Plats för kommentar'''
    return render_template('index.html', data=data)
