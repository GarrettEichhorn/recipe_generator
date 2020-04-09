from flask import Flask
from flask_cors import CORS
import pandas as pd
from python_files.search_engine import return_relevant_recipes
import json

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the RECIPERFECT search API!<br/>")

@app.route("/api/search/<query>")
def search_query(query=None):

    try:
        results = return_relevant_recipes(query)
        df_to_dict = results.to_dict('r')
        data = json.dumps(df_to_dict, ensure_ascii=False, indent=4)

        return (
            data
        )

    except Exception as e:
        return (
            f"{e}"
    )

if __name__ == '__main__':
    app.run()