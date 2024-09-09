import sys
from Expense import Expense
from Categories import Category


def main(name, category, amount):
    expense_file_path = "csv/expenses.csv"
    write_to_file(name, category, amount, expense_file_path)


def write_to_file(name, category, amount, file):
    record = Expense(name, category, amount)
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
