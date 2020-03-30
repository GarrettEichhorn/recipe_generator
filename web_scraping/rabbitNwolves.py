import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Function to grab ingredients and instructions from rabbit and wolves inner-page
def grab_details_rabbwolf(url):

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    recipe_ingredients_detail = soup.find_all('li', attrs={'class': 'wprm-recipe-ingredient'})
    ingredients_list = []

    for ingredients in recipe_ingredients_detail:
        ingredients_list.append(ingredients.text)

    recipe_instructions_detail = soup.find_all('li', attrs={'class': 'wprm-recipe-instruction'})
    instructions_list = []

    for instruction in recipe_instructions_detail:
        instructions_list.append(instruction.text)

    image_detail = soup.find("div", attrs={'class': 'wprm-recipe-image'})

    try:
        if image_detail.img['src']:
            image = image_detail.img['src']
            image = str(image.replace("150", "500"))

    except Exception as e:

        image = None
        pass

    return ingredients_list, instructions_list, image

# Function to grab link from rabbit and wolves recipes page
def rabbitandwolves():

    my_dict = {}

    url = 'https://www.rabbitandwolves.com/category/entrees/'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        recipes = soup.find_all('a', class_='entry-title-link')

        for recipe in recipes:

            recipe_link = recipe['href']
            my_dict[recipe.text] = [recipe_link]

        # Iterate through to the next page
        browser.click_link_by_partial_text('Next Page »')

    for recipe_name in my_dict:

        link = my_dict[recipe_name]
        details = grab_details_rabbwolf(link[0])
        ingredients, instructions, image = details

        my_dict[recipe_name].append(ingredients)
        my_dict[recipe_name].append(instructions)
        my_dict[recipe_name].append(image)

        print(my_dict)

    return my_dict

dict = rabbitandwolves()

df = pd.DataFrame(dict.values(), index=dict.keys(), columns=['Link', 'Ingredients', 'Instructions', 'Image'])

df.to_excel('/Users/garretteichhorn/Desktop/github_repos/recipe_generator/excel_files/rabbitandwolves_recipes.xlsx')