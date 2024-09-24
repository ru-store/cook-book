with (open("cook.txt") as file):
    cook_book = {}
    for dish in file:
        name_dish = dish.strip()
        number_ingredients = int(file.readline())
        ingredients = []
        for number in range(number_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(" | ")
            ingredients.append({"ingredient": ingredient_name, "quantity": quantity, "measure": measure})
            cook_book[name_dish] = ingredients
            file.readline()


