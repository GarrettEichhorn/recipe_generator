import pandas as pd
import os
from pprint import pprint
import json

rootdir = '/Users/garretteichhorn/Desktop/github_repos/recipe_generator/excel_files'

# Function to concat files, assuming same structure
def concat_files(root_path):

    df_list = []

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            df = pd.read_excel(os.path.join(subdir, file), index=False)
            df_list.append(df)

    for df in df_list:
        df.columns = ["Recipe_Name", "Link", "Summary", "Ingredients", "Instructions", "Image"]

    df1 = pd.concat(df_list).reset_index(drop=True)

    return df1

# Function to dump files to .js format
def save_to_json(dataframe):

    # Drop null records
    df = dataframe[dataframe['Image'].notna()]

    df_to_dict = df.to_dict('r')
    with open('/Users/garretteichhorn/Desktop/github_repos/recipe_generator/static/js/data.js', 'w') as json_file:
        json.dump(df_to_dict, json_file, ensure_ascii=False, indent=4)

df = concat_files(rootdir)
save_to_json(df)
