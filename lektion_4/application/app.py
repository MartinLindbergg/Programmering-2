from flask import Flask, render_template, request
import urllib.request
import ssl
import json
import pandas as pd



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
    
    year = request.form["year"]
    country_code = request.form["countrycode"]

    context = ssl._create_unverified_context()
    data_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    
    json_data = urllib.request.urlopen(data_url, context=context).read()
    data = json.loads(json_data)

    # Läser in tolkad json i ett DataFrame
    df = pd.DataFrame(data)
    table_data = df.to_html(columns=["date","localName"],classes="table p-5",justify="left")

    return render_template('index.html', data=table_data)


# Se till att vara i rätt map (application) och har aktiverat venv
# flask --app app run --debug För att starta programmet från terminalen