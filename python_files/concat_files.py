import pandas as pd
import os

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