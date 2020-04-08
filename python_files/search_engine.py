from python_files.concat_files import rootdir, concat_files

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Concatenate files and drop null values
df = concat_files(rootdir)
dataframe = df[df['Image'].notna()]

# Combine text columns
dataframe["text"] = dataframe["Recipe_Name"] + " " + dataframe["Summary"]

# Cast as a list of values for calculating weights
text_data= dataframe.text.values.tolist()

# Calculate TF-IDF matrix
def tf_idf(search_keys, data):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_weights_matrix = tfidf_vectorizer.fit_transform(data)
    search_query_weights = tfidf_vectorizer.transform([search_keys])

    return search_query_weights, tfidf_weights_matrix

# Calculate the cosine similarity between search query and TF-IDF vectors
def cos_similarity(search_query_weights, tfidf_weights_matrix):
    cosine_distance = cosine_similarity(search_query_weights, tfidf_weights_matrix)
    similarity_list = cosine_distance[0]

    return similarity_list

# Calculate number of relevant vectors
def calculate_num_vectors(cosine_similarity):

    num = 0
    for i in cosine_similarity:
        if i != 0.0:
            num += 1
    return num

# Calculate the most relevant vectors
def most_similar(similarity_list, N):

    most_similar = []

    while N > 0:
        tmp_index = np.argmax(similarity_list)
        most_similar.append(tmp_index)
        similarity_list[tmp_index] = 0
        N -= 1

    return most_similar

# Create weights at specific index for quick retrieval
def create_matrix_dict(cosine_similarity):

    matrix_dict = {}

    iter = 0
    for i in cosine_similarity:
        matrix_dict[iter] = i
        iter += 1

    return matrix_dict

# -----------
# Return the recipes with relevant search term
def return_relevant_recipes(search_term):

    # Create local variables
    search, matrix = tf_idf(search_term, text_data)
    cosine_sim_list = cos_similarity(search, matrix)
    num_relevant_vectors = calculate_num_vectors(cosine_sim_list)
    dictionary = create_matrix_dict(cosine_sim_list)
    list_of_most_similar = most_similar(cosine_sim_list, num_relevant_vectors)

    df = pd.DataFrame()

    for index in list_of_most_similar:

        recipe = dataframe.iloc[index]

        if df.empty:

            to_dataframe = recipe.to_frame()
            df = to_dataframe.T

        else:
            to_dataframe = recipe.to_frame()
            df = pd.concat([df, to_dataframe.T], join='outer')

    columns = ['Recipe_Name', 'Link', 'Summary', 'Ingredients', 'Instructions', 'Image']

    return df[columns]

