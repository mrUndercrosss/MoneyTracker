# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from ExpenseTracking import *
from IncomeTracking import *

def get_graphic(Middle_panel):
    expense = get_expesnses_from_file()
    income = get_incomes_from_file()
    def get_actual_data(transaction_list, tranz_t):
        """
        ������� ���������� ������ �� ����������, ������� ���� ��������� � ��������� ������
        :return: ������ �������� ����������
        """
        indices_to_delete = []
        date = 'expense_date' if tranz_t == 'e' else 'income_date'
        amount = 'expense_amount' if tranz_t == 'e' else 'income_amount'
        for index, expen in enumerate(transaction_list):
            if (Middle_panel.period_date[0] in expen.get(date)) or (expen.get(date) in Middle_panel.period_date):
                continue
            else:
                indices_to_delete.append(index)
        for idx in reversed(indices_to_delete):
            del transaction_list[idx]

        endlessly = {}
        actual_transaction_list = []
        trans = []
        for transaction in transaction_list:
            trans.append({'date': transaction.get(date), 'amount': transaction.get(amount)})
        for tran in trans:
            date = tran.get('date')
            amount = int(tran.get('amount'))
            if date in endlessly.keys():
                endlessly[date] += amount
            else:
                endlessly[date] = amount

        for key in endlessly.keys():
            expenses_dict = {'����': key, '�����': endlessly[key]}
            actual_transaction_list.append(expenses_dict)

        return actual_transaction_list

    expenses = get_actual_data(transaction_list=expense, tranz_t='e')
    if not expenses:
        expenses = [{"����": "", "�����": 0}]
    incomes = get_actual_data(transaction_list=income, tranz_t='i')
    if not incomes:
        incomes = [{"����": "", "�����": 0}]

    expenses_df = pd.DataFrame(expenses)
    incomes_df = pd.DataFrame(incomes)

    # ����������� ������ �� ����
    merged_df = expenses_df.merge(incomes_df, on='����', how='outer')

    # ���������� ���������
    merged_df.fillna(0, inplace=True)

    merged_df['�������'] = merged_df['�����_y'] - merged_df['�����_x']
    merged_df.rename(columns={'�����_y': '�����', '�����_x': '������'}, inplace=True)

    figure = plt.Figure(figsize=(12, 6))
    ax = figure.add_subplot(111)

    ax.plot(merged_df['����'], merged_df['�����'], label='������', marker='o', linestyle='-', color='green')
    ax.plot(merged_df['����'], merged_df['������'], label='�������', marker='o', linestyle='--', color='red')
    ax.plot(merged_df['����'], merged_df['�������'], label='�������', marker='o', linestyle=':', color='blue')

    ax.set_xlabel('����')
    ax.legend()
    ax.grid(True)
    ax.set_title('������ �������, �������� � �������')

    canvas = FigureCanvasTkAgg(figure, Middle_panel.graph_frame.frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

