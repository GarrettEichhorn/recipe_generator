import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Function to grab ingredients and instructions from bon appetit inner-page
def grab_recipe_details(url):

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Extract Summary
    recipe_summary = soup.find('h2', attrs={'class': 'dek--basically'})
    if recipe_summary is not None:
        summary = recipe_summary.text
    else:
        summary = ""

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

    return summary, ingredients_list, instructions_list, img

# Function to grab link from bon appetit recipes page
def bonappetit():

    recipe_dict = {}

    url = 'https://www.bonappetit.com/gallery/simple-recipes-five-ingredients'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        recipes = soup.find_all('figcaption', class_='gallery-slide--not-ordered gallery-slide--left gallery-slide__caption')

        for recipe in recipes:

            recipe_link = recipe.div.a['href']
            recipe_dict[recipe.div.a.h2.text] = [recipe_link]

    for recipe_name in recipe_dict:

        link = recipe_dict[recipe_name]

        time.sleep(55)

        details = grab_recipe_details(link[0])
        summary, ingredients, instructions, image = details

        recipe_dict[recipe_name].append(summary)
        recipe_dict[recipe_name].append(ingredients)
        recipe_dict[recipe_name].append(instructions)
        recipe_dict[recipe_name].append(image)

        print(recipe_dict)

    return recipe_dict

recipe_dict = bonappetit()

df = pd.DataFrame(recipe_dict.values(), index=recipe_dict.keys(), columns=['Link', 'Summary', 'Ingredients', 'Instructions', 'Image'])

df.to_excel('/Users/garretteichhorn/Desktop/github_repos/recipe_generator/excel_files/bon_appetit_recipes.xlsx')

