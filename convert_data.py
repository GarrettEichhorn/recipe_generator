import pandas as pd
import os
from pprint import pprint
import json

file_path = os.path.join("excel_files", "bon_appetit_recipes.xlsx")
df = pd.read_excel(file_path, index=False)
columns = ["Recipe_Name", "Link", "Ingredients", "Instructions", "Image"]
df.columns = columns

df = df.infer_objects()
print(df.dtypes)


df_to_dict = df.to_dict('r')
with open('templates/static/js/data1.js', 'w') as json_file:
    json.dump(df_to_dict, json_file, ensure_ascii=False, indent=4)