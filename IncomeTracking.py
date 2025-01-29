from Expense import Expense


def write_to_file(name, category, amount, user_id, date):
    income_file_path = "csv/incomes.csv"
    record = Expense(name=name, category=category, amount=amount, date=date, user_id=user_id)
    print(f"Записываем {record.name} в {income_file_path}")
    with open(income_file_path, "a") as f:
        f.write(f"{record.name},{record.category},{record.amount},{record.user_id},{record.date} \n")


def get_incomes_from_file():
    income_file_path = "csv/incomes.csv"
    incomes = []
    with open(income_file_path, "r", encoding="windows-1251") as f:
        lines = f.readlines()
        for line in lines:
            if len(line) == 1:      # Видимо из-за кодировок он теперь в строках видит \n, минипроверка
                continue
            income_name, income_category, income_amount, user_id, income_date = line.strip().split(",")
            income_in_dict = {'income_name': income_name,
                              'income_amount': income_amount,
                              'comment': 'comment',
                              'user_id': user_id,
                              'income_date': income_date,
                              'income_category': income_category}
            incomes.append(income_in_dict)

    return incomes


def clear_income_file():
    income_file_path = "csv/incomes.csv"
    with open(income_file_path, 'r+') as f:
        f.truncate(0)