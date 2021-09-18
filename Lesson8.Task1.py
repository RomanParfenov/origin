
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


def look_eat_book(book):
         for i in book:
          print(i)
          pprint(book[i])

look_eat_book(eat_book('recipes.txt'))









