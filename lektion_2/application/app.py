
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def lista():
    dict = {
    "landsdel": ["götaland", "svealand", "norrland"],
    "landskap": ["östergötland", "västergötland", "södermanland"],
    "stad":     ["linköping", "motala", "mjölby", "mariefred", "nyköping", "piteå", "sandviken", "sollefteå", "kramfors", "örnsköldsvik"]
            }

    df = pd.DataFrame(dict)
    html = df.to_html()



@app.route("/")
def home():
    return "hej"




if __name__ == "__main__":
    app.run(debug=True)

