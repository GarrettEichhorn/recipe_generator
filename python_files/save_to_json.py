import pandas as pd
import os
import json

from python_files.concat_files import concat_files
rootdir = '/Users/garretteichhorn/Desktop/github_repos/recipe_generator/excel_files'

# Function to dump files to .js format
def save_to_json(dataframe, output_name):

    # Drop null records
    df = dataframe[dataframe['Image'].notna()]

    df_to_dict = df.to_dict('r')
    with open(f'/Users/garretteichhorn/Desktop/github_repos/recipe_generator/static/js/{output_name}', 'w') as json_file:
        json.dump(df_to_dict, json_file, ensure_ascii=False, indent=4)

df = concat_files(rootdir)
save_to_json(df, "data.js")
