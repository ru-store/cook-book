with open("cook.txt") as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        number_ingredients = int(file.readline())
        ingredients = []
        for number in range(number_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({'ingredient': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name_dish] = ingredients
    print(cook_book)


