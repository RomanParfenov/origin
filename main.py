

from application.salary import calculate_salary
from application.database.people import data_employee
from datetime import datetime


def time_now(clock):
    print(f'Время на текущий момент: {clock}')

class Accountant:
    def __init__(self, name, password):
        self.name = name
        self.password = password


def main():
    accountant = Accountant('Tonny', '007')
    print('Доброе утро', accountant.name)
    time_now(datetime.now())
    calculate_salary(data_employee[0], data_employee[1], data_employee[2])
    pass

if __name__ == '__main__':
    main()


