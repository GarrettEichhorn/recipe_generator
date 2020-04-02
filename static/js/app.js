const recipeData = data;

var random_int = Object.keys(recipeData)[Math.floor(Math.random()*Object.keys(recipeData).length)];

var specific_recipe = recipeData[random_int];

var recipe_var = specific_recipe;
var recipe_keys = Object.keys(recipe_var);
var recipe_values = Object.values(recipe_var);

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

const ingredients_table = d3.select("#Ingredients");

function buildTable(data) {
  // First, clear out any existing data
  ingredients_table.html("");

  document.getElementById("Title").innerHTML = specific_recipe.Recipe_Name;
  document.getElementById("Instructions").innerHTML = res;

  // Change image sizing
  console.log(specific_recipe.Image);
  document.getElementById("image1").src = specific_recipe.Image;

  for (var i = 0; i < ingredients.length; i++) {

      // Append a row to the table body
      const row = ingredients_table.append("tr");
      let cell = row.append("tr");
      cell.text(ingredients[i]);
    }
}

function handleClick() {

  window.location.reload();
}

// Attach an event to listen for the form button
d3.selectAll("#filter-btn").on("click", handleClick);

// Build the table when the page loads
buildTable(specific_recipe);