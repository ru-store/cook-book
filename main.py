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

def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}
    for dish in dishes:
        if dish in cook_book:
            for eating in cook_book[dish]:
                list_products.values({cook_book[measure]}, {int(cook_book[quantity])} * int(person_count))
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return list_products

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



