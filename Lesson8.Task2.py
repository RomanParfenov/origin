
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
     products = {}
     for dis in dishes:
          meas = []
          for i in list(data.get(dis)):
               ing = i['ingredient_name']
               quant = i['quantity']*person_count
               mes = i['measure']
               meas.append(mes)
               if ing in products:
                    products[ing] += quant
               else:
                    products[ing] = quant

     solut = [{'ingredient_name': j, "quantity": q} for j, q in products.items()]

     for s in solut:
          for k in meas:
               s["measure"] = k
          print(s)


et_shop_list_by_dishes(eat_book('recipes.txt'), ['Фахитос', 'Фахитос'], 1)





