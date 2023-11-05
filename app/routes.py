from flask import render_template, request, jsonify
from app import app
from app import model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    name = request.form['name']
    servings = int(request.form['servings'])
    time = int(request.form['time'])
    cuisine = request.form['cuisine']
    course = request.form['course']
    diet = request.form['diet']

    # Send the input data to your recommendation model in model.py
    recommendations = model.get_recommendations(name, time, servings, cuisine, course, diet)

    return jsonify(recommendations)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    # Add logic to fetch and display the details of the recipe with the given recipe_id
    # You can fetch recipe details from your data source
    recipe_data = model.get_recipe_by_id(recipe_id)
    #Clean the recipe data to remove extra information
    cleaned_recipe = {
        'name': recipe_data['name'].iloc[0],
        'servings': recipe_data['servings'].iloc[0],
        'time': recipe_data['time'].iloc[0],
        'cuisine': recipe_data['cuisine'].iloc[0],
        'course': recipe_data['course'].iloc[0],
        'diet': recipe_data['diet'].iloc[0],
        'instructions': recipe_data['instructions'].iloc[0],
        'ingredients': recipe_data['ingredients'].iloc[0]
    }

    return render_template('recipe.html', recipe=cleaned_recipe)
