#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    curr_min = 100000
    for item in recipe:
        if not item in ingredients or recipe[item] > ingredients[item]:
            return 0
        else:
            if ingredients[item] // recipe[item] < curr_min:
                curr_min = ingredients[item] // recipe[item]

    return curr_min


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
