# Web Link

[Recipe Generator](https://garretteichhorn.github.io/recipe_generator/)

This application was created to make Sunday meal planning easier! Gone are the days of traversing the internet for recipes using vague search criteria, inundated by too-many choices and irrelevant results. I grabbed recipes from my favorite online providers and amalgamated them for quick retrieval to generate recipe ideas for the week.

-----

This app scrapes data from several popular recipe websites...

* [Bon Appétit](https://www.bonappetit.com/)
    ** Scraped with BS4 via Splinter (abstract layer for Selenium)  
* [Half Baked Harvest](https://www.halfbakedharvest.com/)
    ** Scraped with BS4 via Splinter  
* [Ambitious Kitchen](https://www.ambitiouskitchen.com/)
    ** Scraped with BS4 via requests  

... and amalgamates the data for quick retrieval via website (linked above).

-----

Websites are scraped with different technology to demonstrate functional expertise.

You can run the app (in a serverless environment) by visiting the link above. To query the data via search criterion, please download the repository and run the app.py file via flask directly from the terminal. Then, visit the link and search until your heart's content!
