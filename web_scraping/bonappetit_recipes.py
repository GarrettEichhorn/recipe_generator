import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Function to grab ingredients and instructions from bon appetit inner-page
def grab_details_bonappetit(url):

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Extract Ingredients
    recipe_ingredients_detail = soup.find_all('li', attrs={'class': 'ingredient'})
    ingredients_list = []

    for ingredients in recipe_ingredients_detail:
        ingredients_list.append(ingredients.text)

    # Extract Instructions
    recipe_instructions_detail = soup.find_all('li', attrs={'class': 'step'})
    instructions_list = []

    for instruction in recipe_instructions_detail:
        instructions_list.append(instruction.text)

    # Extract Image
    recipe_image_detail = soup.find('img', attrs={'class': 'ba-picture--fit'})
    string = recipe_image_detail['srcset']
    s = str(string)
    img = s[:s.find("1x") - 1]

    return ingredients_list, instructions_list, img

# Function to grab link from bon appetit recipes page
def bonappetit():

    my_dict = {}

    url = 'https://www.bonappetit.com/gallery/simple-recipes-five-ingredients'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        recipes = soup.find_all('figcaption', class_='gallery-slide--not-ordered gallery-slide--left gallery-slide__caption')

        for recipe in recipes:

            recipe_link = recipe.div.a['href']
            my_dict[recipe.div.a.h2.text] = [recipe_link]

    for recipe_name in my_dict:

        link = my_dict[recipe_name]

        time.sleep(40)

        details = grab_details_bonappetit(link[0])
        ingredients, instructions, image = details

        my_dict[recipe_name].append(ingredients)
        my_dict[recipe_name].append(instructions)
        my_dict[recipe_name].append(image)

        print(my_dict)

    return my_dict

dict = bonappetit()

df = pd.DataFrame(dict.values(), index=dict.keys(), columns=['Link', 'Ingredients', 'Instructions', 'Image'])

df.to_excel('excel_files/bon_appetit_recipes.xlsx')

