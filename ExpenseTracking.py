from Expense import Expense


def write_to_file(name, category, amount, user_id, date):
    expense_file_path = "csv/expenses.csv"
    record = Expense(name=name, category=category, amount=amount, date=date, user_id=user_id)
    print(f"Записываем {record.name} в {expense_file_path}")
    with open(expense_file_path, "a") as f:
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
            expense_in_dict = {'expense_name': expense_name,
                               'expense_amount': expense_amount,
                               'comment': 'comment',
                               'user_id': user_id,
                               'expense_date': expense_date,
                               'expense_category': expense_category}

            expenses.append(expense_in_dict)

    return expenses


def clear_expense_file():
    expense_file_path = "csv/expenses.csv"
    with open(expense_file_path, 'r+') as f:
        f.truncate(0)