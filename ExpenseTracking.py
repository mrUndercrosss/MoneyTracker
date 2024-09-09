import sys
from Expense import Expense
from Categories import Category


def main():
    expense_file_path = "csv/expenses.csv"
    # todo: Add the ability to add expense
    expense = add_expenses()
    # todo: Add the ability to add categories
    # Теперь есть такая возможность через класс Category
    # todo: Write their expense to a file
    write_to_file(expense, expense_file_path)
    # todo: Read file and summarize expenses
    expense_list = summarize_expenses(expense_file_path)


def add_category():
    print('You add new category')


def add_expenses():
    """
    Создаёт новую транзакцию, у которой имеются такие параметры, как
    - название транзакции
    - категория транзакции
    - количество потраченных денег
    :return: объект класса Expense
    """
    try:
        expense_name = input("Ну и на что ты потратил деньги?\n")
        if not expense_name:
            raise ValueError
        expense_amount = float(input("Сколько?\n"))
        if not expense_amount:
            expense_amount = 0
    except ValueError as VE:
        print('Можешь по людски отвечать?')
        try:
            expense_name = input("Так на что в итоге ты потратил деньги?\n")
            expense_amount = float(input("Сколько? (здесь надо циферками)\n"))
        except ValueError as VE:
            print('Ясно, с быдлом дело имею')
            exit()
    expense_categories = Category().category_list
    while True:
        print("Выбери категорию:")
        for i, expense_category in enumerate(expense_categories):
            print(f' {i + 1}: {expense_category}')
        value_range = f"от 1 до {len(expense_categories)}: "
        select_index = int(input(f"Цифра {value_range}")) - 1
        if select_index in range(len(expense_categories)):
            selected_category = expense_categories[select_index]
            new_expense = Expense(name=expense_name, category=selected_category,
                                  amount=expense_amount)
            return new_expense
        else:
            print("Ты инвалид чтоль?", end=' ')


def write_to_file(record: Expense, file):
    print(f"Записываем {record.name} в {file}")
    with open(file, "a") as f:
        f.write(f"{record.name},{record.category},{record.amount} \n")


def summarize_expenses(expend_file):
    expenses = []
    with open(expend_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)
    expense_categories = []
    categories = Category().category_list
    for category in categories:
        key = category
        expense_categories.append({key: []})
    for expense in expenses:
        for category in expense_categories:
            key = list(category.keys())[0]
            if expense.category == key:
                category.get(key).append(expense.amount)
                break
    return expense_categories


if __name__ == "__main__":
    main()