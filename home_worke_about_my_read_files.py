from pprint import pprint


def my_cook_book(file_main):
    with open(file_main, 'r', encoding='utf-8') as file_ingredients:
        menu = {}
        for line in file_ingredients:
            dish_name = line[:-1]
            counter = file_ingredients.readline().strip()
            list_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file_ingredients.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_ingridient.append(dish_items)
                cook_book = {dish_name: list_ingridient}
                menu.update(cook_book)
            file_ingredients.readline()
    return(menu)
my_cook_book('my_recipes.txt')


def get_shop_list_by_dishes(dishes, persons=int):
    menu = my_cook_book('my_recipes.txt')
    print('Получившееся меню:')
    pprint(menu)
    print()
    products_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if products_list.get(item['ingredient_name']):
                    extra_item = (int(products_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    products_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    products_list.update(items_list)
        print(f"Для приготовления блюд на следующее количество персон: {persons}, необходимо купить следующие ингридиенты:")
        pprint(products_list)
    except KeyError:
        print("Такое название блюда отсутствует, проверьте список блюд и попробуйте ввести нужное название блюда!")
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


import os


def create_unified_list(directory):
    file_list = os.listdir(directory)
    unified_list = []
    for file in file_list:
        with open(directory + "/" + file, encoding='utf-8') as cur_file:
            unified_list.append([file, 0, []])
            for line in cur_file:
                unified_list[-1][2].append(line.strip())
                unified_list[-1][1] += 1
    return sorted(unified_list, key=lambda x: x[2], reverse=True)


def create_directory_file(directory, filename):
    with open(filename + '.txt', 'w+', encoding='utf-8') as newfile:
        for file in create_unified_list(directory):
            newfile.write(f'File name: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')
create_directory_file('directory', 'directory_text')
