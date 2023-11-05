from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import numpy as np

# Sample recipes (replace with your actual data)
recipes = pd.read_csv('recipes.csv', engine='python')

# Weights for each feature
weights = {
    'name': 0.35,
    'servings': 0.1,
    'time': 0.3,
    'cuisine': 0.15,
    'course': 0.1,
    'diet': 0.1
}

# Function to return recipe based on recipe ID
def get_recipe_by_id(recipe_id):
    return recipes[recipes.id==recipe_id]

# Function to calculate cosine similarity between user input and recipes
def get_cosine_similarity(user_input, recipes):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Create a matrix with feature vectors for each recipe
    features = recipes[['name', 'servings', 'time', 'cuisine', 'course', 'diet']].fillna('').astype(str)

    tfidf_matrix = tfidf_vectorizer.fit_transform(features.apply(lambda x: ' '.join(x), axis=1))
    
    # Transform the user input into a list of strings
    user_vector = tfidf_vectorizer.transform([' '.join(user_input.values())])

    cosine_similarities = linear_kernel(user_vector, tfidf_matrix)
    return cosine_similarities

# Function to get recipe recommendations based on user input
def get_recommendations(name, servings, time, cuisine, course, diet):
    user_input = {
        'name': name.lower(),
        'servings': str(servings),
        'time': str(time),
        'cuisine': cuisine.lower(),
        'course': course.lower(),
        'diet': diet.lower()
    }

    # Calculate cosine similarity for each feature
    similarity = get_cosine_similarity(user_input, recipes)

    # Calculate a weighted sum of similarities for each feature
    combined_scores = np.sum([similarity * weight for feature, weight in weights.items()], axis=0)

    # Get the indices that rank the recipes
    sorted_indices = combined_scores.argsort()[0][::-1]

    # Get the top 9 recipe recommendations
    top_recipe_indices = sorted_indices[:30]
    recommended_recipes = [recipes.iloc[i].to_dict() for i in top_recipe_indices]

    return recommended_recipes
