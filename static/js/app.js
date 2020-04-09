// Grab data from the static JSON file
var recipeData = data;

// Function to calculate random integer for recipe
function generateRandomInteger(data) {

    // Select a random recipe using MATH
    var random_int = Object.keys(recipeData)[Math.floor(Math.random()*Object.keys(recipeData).length)];
    var specific_recipe = recipeData[random_int];

    return specific_recipe
}

// Grab Ingredients in HTML
const ingredients_table = d3.select("#Ingredients");

// Function to build the data using a parameter data
function buildTable(data) {

    // First, clear out any existing data
    ingredients_table.html("");

    specific_recipe = generateRandomInteger(data);

    // Instantiate relevant variables for quick retrieval
    var recipe_keys = Object.keys(specific_recipe);
    var recipe_values = Object.values(specific_recipe);

    // basic string replace to 'clean-up' and format array response for ingredients and instructions
    for (var i = 0; i < recipe_keys.length; i++) {

        if (i === 3) {
            var strip = recipe_values[i].replace(/[\])}[{(]/g, '');
            var ingredients = strip.split("', '");
        }
        else if (i === 4) {
            var strip = recipe_values[i].replace(/[\])}[{(]/g, '');
            var instructions = strip.split("', '");
            var res = instructions.join(" <br> ");
        }
    }

  document.getElementById("Title").innerHTML = specific_recipe.Recipe_Name;
  document.getElementById("Instructions").innerHTML = res;

  // Image sizing for different versions...
  var image_string = specific_recipe.Image;
  var image_substring = "725x725.jpg";

  if (image_string.includes(image_substring) === true) {

      var image_class = document.getElementById("image_responsive");
      image_class.setAttribute("class", "embed-responsive embed-responsive-4by3");
  }

  document.getElementById("image1").src = specific_recipe.Image;

  for (var i = 0; i < ingredients.length; i++) {

      // Append a row to the table body
      const row = ingredients_table.append("tr");
      let cell = row.append("tr");
      cell.text(ingredients[i]);
    }
}

// Function to handle the search criteria via button click
function handleClickSearch() {

    const query = d3.select('#search_query').property("value");

    if (query) {
        console.log(query);
        document.getElementById("search_query").placeholder=query;

        var url = "https://reciperfect.herokuapp.com/api/search/";
        var updated_url = url + query;

        fetch(updated_url)
          .then(function (response) {
            return response.json();
          })
          .then(function (data) {

                recipeData = data;
                buildTable(recipeData);
                var num_query_results = recipeData.length;

                document.getElementById("search_num").innerHTML = "Your query returned " + num_query_results + " results.";
          })

          .catch(function (err) {
            console.log(err);
          });
    }
}

// Function to generate new recipes for random generator
function handleClickRandom() {
  window.location.reload();
}

// Attach an event to listen for the search recipes button
d3. select("#search-btn").on("click", handleClickSearch);

// Attach an event to listen for the generate random recipe button
d3.select("#filter-btn").on("click", handleClickRandom);

// Build the table when the page loads
buildTable(recipeData);
