with open("cook.txt") as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        quantity_ingredients_in_dish = int(file.readline())
        ingredients = []
        for counter in range(quantity_ingredients_in_dish):
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
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient']
                quantity = ingredient['quantity']*person_count
                measure = ingredient['measure']
                if ingredient_name in list_products:
                    list_products[ingredient_name]['quantity'] += quantity
                else:
                    list_products[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f'Блюда {dish} нет в книге рецептов')
            return list_products


shop = get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Омлет'], 4)
print(shop)



