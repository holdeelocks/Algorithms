#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    curr_min = 100000
    for item in ingredients:
        if not item in recipe:
            return 0
        else:
            if ingredients[item] < recipe[item]:
                return 0
            else:
                ingredients[item] = recipe[item] // ingredients[item]
                if ingredients[item] < curr_min:
                    curr_min = recipe[item]

    return curr_min


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
