
from pprint import pprint


def eat_book(file_name: str) -> dict:
     result: dict = dict()
     with open(file_name) as file:
          for line in file:
               dish = line.strip()
               control_quantity = int(file.readline())
               dish_list = []
               for items in range(control_quantity):
                    ingredient_name, quantity, measure = file.readline().split('|')
                    dish_list.append({"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()})
               result[dish] = dish_list
               file.readline()
     return result


def et_shop_list_by_dishes(data, dishes, person_count):
     for dis in dishes:
          for i in list(data.get(dis)):
               i['quantity'] = i['quantity']*person_count
               print(i)


et_shop_list_by_dishes(eat_book('recipes.txt'), ['Утка по-пекински', 'Омлет', 'Фахитос'], 2)







