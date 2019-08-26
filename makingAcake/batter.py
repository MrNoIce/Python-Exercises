def make_better_cake_batter(ingredients):
    cake_batter_mass = 0
    for value in ingredients.values():
        cake_batter_mass += value

    return cake_batter_mass