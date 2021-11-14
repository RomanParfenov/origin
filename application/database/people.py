
def name_employee():
    name = input("Введите имя сотрудника \n")
    department = input("Введите имя отдела \n")
    salary = float(input('Введите величину зарплаты \n'))
    return [salary, department, name]

data_employee = name_employee()