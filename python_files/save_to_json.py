import json
import os

from python_files.concat_files import concat_files, root_path

# Function to dump files to .js format
def save_to_json(dataframe, output_path, output_name):

    # Drop null records
    df = dataframe[dataframe['Image'].notna()]

    df_to_dict = df.to_dict('r')
    with open(f'{output_path}/{output_name}', 'w') as json_file:
        json.dump(df_to_dict, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    df = concat_files(root_path)
    output_path = os.path.join('..', 'static', 'js')
    file_name = "data.js"
    save_to_json(df, output_path, file_name)
