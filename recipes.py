# %%
import pandas as pd

recipes = pd.read_csv('recipes.csv', engine='python', error_bad_lines=False)

# %%
recipes.info(), recipes.shape
recipes.columns

# %%
recipes.head(3)

# %%
recipes.loc[0]

# %%
recipes.id[0]

# %%
recipes.name[0]

# %%
recipes.ingredients[0]

# %%
recipes.prepTime[0]

# %%
recipes.cookTime[0]

# %%
recipes.totalTime[0]

# %%
recipes.servings[0]

# %%
recipes.cuisine[0]

# %%
recipes.course[0]

# %%
recipes.diet[0]

# %%
recipes.instructions[0]

# %%
recipes.image[0]

# %%
# Function for counting Null values 
def countNullValues(col):
  c = 0
  for i in col:
    if(i != i):
      c+=1
  return c

recipes.isnull().sum()


# %%
recipes.isnull().sum()

# %%
def reformatIngredients(columnTitle):
    L = []
    for i in columnTitle:
        L.append(str(i).split(','))
    return L

# %%
def reformatInstructions(columnTitle):
    L = []
    for i in columnTitle:
        L.append(str(i).split('. '))
    return L

# %%
recipes.ingredients = reformatIngredients(recipes.ingredients)
recipes.instructions = reformatInstructions(recipes.instructions)

# %%
recipes.instructions

# %%
cuisineCat = recipes.cuisine.value_counts()

# %%
courseCat = recipes.course.value_counts()

#%%
dietCat = recipes.diet.value_counts()
temp = recipes[recipes.id==8]

for item in temp.instructions:
    for i in item:
        print(i)

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
features = recipes[['name', 'servings', 'totalTime', 'cuisine', 'course', 'diet']].fillna('').astype(str)
print(features)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(features.apply(lambda x: ' '.join(x), axis=1))
