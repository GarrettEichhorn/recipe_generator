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

... and stores the data for quick retrieval via website (linked above).

-----

Websites are scraped with different technology to demonstrate functional expertise.

The app calls an api built on heroku that references a custom search engine. You can view the [source code](https://github.com/GarrettEichhorn/recipe_api_app) here!
