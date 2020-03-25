import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Function to grab ingredients and instructions from carlsbad craving inner-page
def grab_details_carlsbad(url):

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    recipe_ingredients_detail = soup.find_all('li', attrs={'class': 'wpurp-recipe-ingredient'})
    ingredients_list = []

    for ingredients in recipe_ingredients_detail:
        ingredients_list.append(ingredients.text)

    recipe_instructions_detail = soup.find_all('li', attrs={'class': 'wpurp-recipe-instruction'})
    instructions_list = []

    for instruction in recipe_instructions_detail:
        instructions_list.append(instruction.text)

    return ingredients_list, instructions_list

# Function to grab link from carlsbad cravings recipes page
def carlsbadcraving():

    my_dict = {}

    iterator = 0

    url = 'https://carlsbadcravings.com/recipes/recipe-index/main-course/'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        recipes = soup.find_all('h6', class_='ei-item-title')

        for recipe in recipes:

            recipe_link = recipe.a['href']
            my_dict[recipe.text] = [recipe_link]

    for recipe_name in my_dict:

        link = my_dict[recipe_name]

        details = grab_details_carlsbad(link[0])
        ingredients, instructions = details

        my_dict[recipe_name].append(ingredients)
        my_dict[recipe_name].append(instructions)

        iterator += 1
        print(iterator)
        if iterator % 2 == 0:
            print("Sleep")
            time.sleep(30)

    return my_dict

dict = carlsbadcraving()

df = pd.DataFrame(dict.values(), index=dict.keys(), columns=['Link', 'Ingredients', 'Instructions'])

df.to_excel('carlsbad_craving_recipes.xlsx')
