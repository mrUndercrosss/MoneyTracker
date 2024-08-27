import sys

from Expense import Expense


def main():
    expense_file_path = "expenses.csv"

    # todo: Add the ability to add expense
    expense = add_expenses()

    # todo: Add the ability to add categories

    # todo: Write their expense to a file
    write_to_file(expense, expense_file_path)

    # todo: Read file and sumarize expenses


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

    # todo: выделить категории в отдельный класс, добавить возможность добавлять категории
    expense_categories = [
        'Еда',
        'Транспорт',
        'Развлечения',
        'Компы',
        'Прочее',
        'Test'
    ]

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
    print(f"Записываем {record} в {file}")
    with open(file, "a") as f:
        f.write(f"{record.name},{record.category},{record.amount} \n")



def get_expenses():
    pass


if __name__ == "__main__":
    main()
