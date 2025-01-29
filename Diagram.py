# -*- coding: cp1251 -*-

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from matplotlib.figure import Figure

from Categories import ExpenseCategories, IncomeCategories
from ExpenseTracking import get_expesnses_from_file
from IncomeTracking import get_incomes_from_file
from DB import WorkWithBD

def get_diagram(Middle_panel, user=None):

    """
    Функция выводит диаграмму расходов/доходов за указанный период
    :param user:
    :return:
    """

    cat = ExpenseCategories()
    categories = cat.get_expense_category_dict()
    rows = get_expesnses_from_file()

    if user:
        if user.expenses_or_income == 'i':
            cat = IncomeCategories()
            categories = cat.get_income_category_dict()
            rows = get_incomes_from_file()

    categories_in_diagram = []
    colors = []
    amount = []

    if user:
        category_type = 'expense' if user.expenses_or_income == 'e' else 'income'
    else:
        category_type = 'expense'

    if rows:
        for row in rows:
            category_name = row.get(f'{category_type}_category')
            category_amount = int(row.get(f'{category_type}_amount'))
            category_date = row.get(f'{category_type}_date')
            if (Middle_panel.period_date[0] in category_date) or (category_date in Middle_panel.period_date):
                if category_name not in categories_in_diagram:
                    categories_in_diagram.append(category_name)
                    amount.append(category_amount)
                    colors.append(categories.get(category_name)[0])
                else:
                    ind = categories_in_diagram.index(category_name)
                    amount[ind] += category_amount

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(amount, labels=categories_in_diagram, colors=colors, autopct='%1.1f%%')
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=Middle_panel.diagram_frame.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)




def upgrade_diagram_frame(user):  # todo: Очень на тоненького решение, разобраться бы как передаются названия
    objects_list = []             # todo: для фреймов и канвасов и закрывать конкретные канвасы (Первый анализ показал, что никак)
    for widget in user.main_window.middle_panel.frame.winfo_children():
        objects_list.append(widget)

    for widget in user.main_window.middle_panel.frame.winfo_children():
        if len(widget.children) == 1:
            print()
            list(widget.children.values())[0].destroy() # Что за дикий финт ушами?

    get_diagram(user.main_window.middle_panel, user)