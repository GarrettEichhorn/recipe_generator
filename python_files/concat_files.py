import pandas as pd
import os

root_path = os.path.join('..', 'excel_files')

# Function to concat files, assuming same structure
def concat_files(root_path):

    df_list = []

    for file in os.listdir(root_path):
        df = pd.read_excel(f"{root_path}/{file}", index=False)
        df_list.append(df)

    df1 = pd.concat(df_list).reset_index(drop=True)
    df1.columns = ["Recipe_Name", "Link", "Summary", "Ingredients", "Instructions", "Image"]

    return df1


