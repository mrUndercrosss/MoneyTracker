from Expense import Expense
from DB import *

db = WorkWithBD()


def write_expenses(name, category, amount, user_id, date):
    expense_file_path = "csv/expenses.csv"
    date = date if date else ''
    if user_id and False:           #Пока не могу починить запись в бд - будет висеть False
        print(f'Name:{name}, nameType:{type(name)}')
        print(f'Category:{category}, categoryType:{type(category)}')
        print(f'Amount: {amount}, amountType{type(amount)}')
        print(f'Date:{date}, dateType:{type(date)}')

        db.write_to_bd(name=name, category=category, amount=amount, user_id=user_id, date=date)

    else:
        write_to_file(name=name, category=category, amount=amount, user_id=user_id, date=date, file=expense_file_path)


def write_to_file(name, category, amount, user_id, date, file):
    record = Expense(name=name, category=category, amount=amount, date=date, user_id=user_id)
    print(f"Записываем {record.name} в {file}")
    with open(file, "a") as f:
        f.write(f"{record.name},{record.category},{record.amount},{record.user_id},{record.date} \n")


def get_expesnses_from_file():
    expense_file_path = "csv/expenses.csv"
    expenses = []
    with open(expense_file_path, "r", encoding="windows-1251") as f:
        lines = f.readlines()
        for line in lines:
            if len(line) == 1:      #Видимо из-за кодировок он теперь в строках видит \n, минипроверка
                continue
            expense_name, expense_category, expense_amount, user_id, expense_date = line.strip().split(",")
            expense_in_list = ['expense_id', expense_name, expense_amount, 'comment', 'user_id', expense_date, expense_category]
            expenses.append(expense_in_list)

    return expenses
