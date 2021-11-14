
def calculate_salary(salary, department, name):
    if(salary > 50000):
        tax = 0.15*salary
        netsalary = salary - tax
        print(f'Заработная плата сотрудника {name} отдела {department} составляет: {netsalary}',
        f'Налоговые выплаты составляют {tax}', sep="\n")

    else:
        netsalary = salary
        print(f'Заработная плата сотрудника {name} отдела {department} составляет: {netsalary}',
        f'Налог не удерживается', sep="\n")