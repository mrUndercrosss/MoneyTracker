# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from ExpenseTracking import *
from IncomeTracking import *

def get_graphic(Middle_panel, user=None):
    expense = get_expesnses_from_file()
    income = get_incomes_from_file()
    def get_actual_data(transaction_list):
        """
        Функция возвращает только те транзакции, которые были совершены в указанный период
        :return: список словарей транзакций
        """
        indices_to_delete = []
        for index, expen in enumerate(transaction_list):
            if (Middle_panel.period_date[0] in expen[-2]) or (expen[-2] in Middle_panel.period_date):
                continue
            else:
                indices_to_delete.append(index)
        for idx in reversed(indices_to_delete):
            del transaction_list[idx]

        endlessly = {}
        actual_transaction_list = []
        trans = []
        for transaction in transaction_list:
            trans.append(f'{transaction[-2][-4:]}-{transaction[-2][3:5]}-{transaction[-2][:2]}:{int(transaction[2])}')
        for tran in trans:
            date = tran.split(':')[0]
            amount = int(tran.split(':')[1])
            if date in endlessly.keys():
                endlessly[date] += amount
            else:
                endlessly[date] = amount

        for key in endlessly.keys():
            expenses_dict = {'Дата': key, 'Сумма': endlessly[key]}
            actual_transaction_list.append(expenses_dict)

        return actual_transaction_list


    # Преобразование данных в DataFrames

    expenses = get_actual_data(expense)
    if not expenses:
        expenses = [{"Дата": "", "Сумма": 0}]

    incomes = get_actual_data(income)
    if not incomes:
        incomes = [{"Дата": "", "Сумма": 0}]

    expenses_df = pd.DataFrame(expenses)
    incomes_df = pd.DataFrame(incomes)

    # Объединение данных по дате
    merged_df = expenses_df.merge(incomes_df, on='Дата', how='outer')

    # Заполнение пропусков
    merged_df.fillna(0, inplace=True)

    # Расчет разницы между доходами и расходами
    merged_df['Разница'] = merged_df['Сумма_y'] - merged_df['Сумма_x']

    # Переименовываем столбцы для удобства
    merged_df.rename(columns={'Сумма_y': 'Доход', 'Сумма_x': 'Расход'}, inplace=True)

    # Строим график
    figure = plt.Figure(figsize=(12, 6))
    ax = figure.add_subplot(111)

    # Доходы
    ax.plot(merged_df['Дата'], merged_df['Доход'], label='Доходы', marker='o', linestyle='-', color='green')
    ax.plot(merged_df['Дата'], merged_df['Расход'], label='Расходы', marker='o', linestyle='--', color='red')
    # Разница
    ax.plot(merged_df['Дата'], merged_df['Разница'], label='Разница', marker='o', linestyle=':', color='blue')

    # Настраиваем оси и легенду
    ax.set_xlabel('Дата')
    ax.legend()
    ax.grid(True)
    ax.set_title('График доходов, расходов и разницы')

    # Создаем и размещаем график в контейнере
    canvas = FigureCanvasTkAgg(figure, Middle_panel.graph_frame.frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

