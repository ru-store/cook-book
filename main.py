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
    list_products = []
    for dish in dishes:
        if dish in cook_book[dish]:
            for eating in dish:
                list_products.append({"ingredient": cook_book[dish].get(ingredient_name),
                                      "measure": cook_book[dish].get(measure),
                                      "quantity": cook_book[dish].get(quantity) * (person_count)})
                print(list_products)
        else:
            print(f'Блюда "{dishes}" нет в книге рецептов')


get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Омлет'], 4)



