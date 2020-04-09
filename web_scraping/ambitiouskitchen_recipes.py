"""
Web Scraping with Splinter and requests!
"""

from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd

# -------
# Function to grab page details with Splinter!
def grab_recipe_details(url):

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    recipe_summary = soup.find('div', attrs={'class': 'wprm-recipe-summary'})
    if recipe_summary is not None:
        summary = recipe_summary.text
    else:
        summary = ""

    recipe_ingredients_detail = soup.find_all('li', attrs={'class': "wprm-recipe-ingredient"})
    ingredients_list = []

    for ingredients in recipe_ingredients_detail:
        ingredients_list.append(ingredients.text)

    ingredients_list[:] = [ing.replace('\n', " ") for ing in ingredients_list]

    recipe_instructions_detail = soup.find_all('li', attrs={'class': 'wprm-recipe-instruction'})
    instructions_list = []

    for instruction in recipe_instructions_detail:
        instructions_list.append(instruction.text)

    instructions_list[:] = [instr.replace('\n', " ") for instr in instructions_list]

    image_detail = soup.find("div", attrs={'class': 'wprm-recipe-image'})
    if image_detail is not None:
        image = image_detail.img['src']
    else:
        image = ""

    browser.quit()
    return summary, ingredients_list, instructions_list, image

# -------
# Function to grab recipe links, iterate through recipes, and save to dataframe
def grab_recipe_links():

    recipe_dict = {}
    total_pages = 15

    for i in range(total_pages):

        url = "http://www.ambitiouskitchen.com/wp-admin/admin-ajax.php?" \
              "id=&post_id=4820&slug=recipes&canonical_url=https%3A%2F%2Fwww.ambitiouskitchen.com%2Frecipes%2F" \
              f"&posts_per_page=18&page={i}" \
              "&offset=0&post_type=post&repeater=default&seo_start_page=1" \
              "&theme_repeater=category.php&preloaded=false&preloaded_amount=0&category=recipes" \
              "&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"

        session = requests.Session()
        response = session.get(url)

        html = response.json()
        pretty_html = html['html']
        soup = BeautifulSoup(pretty_html, "html.parser")
        recipes = soup.find_all('div', attrs={'class', 'post-item'})

        for recipe in recipes:

            recipe_name = recipe.h2.text
            recipe_link = recipe.h2.a['href']
            recipe_dict[recipe_name] = [recipe_link]

    for recipe_name in recipe_dict:
        link = recipe_dict[recipe_name]
        details = grab_recipe_details(link[0])
        summary, ingredients, instructions, image = details

        recipe_dict[recipe_name].append(summary)
        recipe_dict[recipe_name].append(ingredients)
        recipe_dict[recipe_name].append(instructions)
        recipe_dict[recipe_name].append(image)

    return recipe_dict


recipe_dict = grab_recipe_links()
df = pd.DataFrame(recipe_dict.values(), index=recipe_dict.keys(), columns=['Link', 'Summary', 'Ingredients', 'Instructions', 'Image'])
df.to_excel('/Users/garretteichhorn/Desktop/github_repos/recipe_generator/excel_files/ambitiouskitchen_recipes.xlsx')
