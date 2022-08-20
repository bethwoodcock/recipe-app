import requests


def recipe_search(ingredient):
    app_id = '18002c98'
    app_key = '46c5a4350bb1b9adaa4e67d27f703c01'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')

    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['url'])
        print()

run()