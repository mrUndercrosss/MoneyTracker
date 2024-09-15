from tkinter import *
from tkinter.ttk import Combobox
from ExpenseTracking import *
from Categories import *
from tkcalendar import DateEntry, Calendar

is_purple = True
expense_file_path = "csv/expenses.csv"

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title('Мяу')
root.resizable(width=False, height=False)
root_width = int(screen_width * 0.75)
root_height = int(screen_height * 0.75)
root.geometry(f"{root_width}x{root_height}")
root.config(bg='Purple')


def create_top_panel():
    """
    Функция создает верхнюю панель, которая содержит кнопку вызова меню,
    кнопку авторизации и название счета
    """
    top_panel_width = root_width
    top_panel_height = int(root_height * 0.1)
    top_panel_frame = Frame(root, width=top_panel_width, height=top_panel_height, highlightthickness=0)
    top_panel_frame.pack(side='top')
    top_panel_frame.pack_propagate(False)

    menu_frame = Frame(top_panel_frame, bg='green', width=int(root_width / 3), height=int(root_height * 0.1),
                       highlightthickness=0)
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left')
    space_frame = Frame(menu_frame, bg='green', width=int(root_width / 24), height=int(root_height * 0.1))
    space_frame.pack(side='left')
    menu_button = Button(menu_frame, text='Кноп', width=int(root_width / 224), command=open_menu)
    menu_button.pack(side='left')
    empty_space = Frame(menu_frame, bg='green', width=int(root_width / 4), height=int(root_height * 0.1))
    empty_space.pack(side='left')

    account_name_frame = Frame(top_panel_frame, bg='green', width=int(root_width / 3), height=int(root_height * 0.1),
                               highlightthickness=0)
    account_name_frame.pack_propagate(False)
    account_name_frame.pack(side='left')
    account_name_button = Button(account_name_frame, text='Основной', width=int(root_width / 3),
                                 height=int(root_height * 0.1), bg='green')
    account_name_button.pack()

    authorization_frame = Frame(top_panel_frame, bg='green', width=int(root_width / 3), height=int(root_height * 0.1),
                                highlightthickness=0)
    top_panel_frame.pack_propagate(False)
    authorization_frame.pack(side='left')
    ex_space = Frame(authorization_frame, bg='green', width=int(root_width / 4), height=int(root_height * 0.1))
    ex_space.pack(side='left')
    authorization_button = Button(authorization_frame, text='Кноп', width=int(root_width / 224))
    authorization_button.pack(side='left')
    space_frame = Frame(authorization_frame, bg='green', width=int(root_width / 24), height=int(root_height * 0.1))
    space_frame.pack(side="left")


def create_middle_panel():
    """
    Создаёт центральную панель
    """

    middle_panel_width = root_width
    middle_panel_height = int(root_height * 0.7)
    middle_panel = Frame(root, width=middle_panel_width, height=middle_panel_height, highlightthickness=0,
                         bg='green')
    middle_panel.pack(side='top')
    middle_panel.pack_propagate(False)

    right_button_panel = Frame(middle_panel, width=round(middle_panel_width*0.05), height=middle_panel_height, bg='green')
    right_button_panel.pack(side='right', fill=BOTH)
    right_button_panel.pack_propagate(False)

    day_button = Button(right_button_panel, text='День\n1')
    day_button.grid(row=1, column=0, sticky='nsew')
    week_button = Button(right_button_panel, text='Неделя\n1')
    week_button.grid(row=2, column=0, sticky='nsew')
    month_button = Button(right_button_panel, text='Месяц\n1')
    month_button.grid(row=3, column=0, sticky='nsew')
    year_button = Button(right_button_panel, text='Год\n1')
    year_button.grid(row=4, column=0, sticky='nsew')
    period_button = Button(right_button_panel, text='Период\n1')
    period_button.grid(row=5, column=0, sticky='nsew')

    for i in range(7):
        right_button_panel.grid_rowconfigure(i, weight=1)

    graph_frame = Frame(middle_panel, width=round(middle_panel_width*0.455), height=middle_panel_height, bg='red')
    graph_frame.pack(side='right', fill=BOTH)
    graph_frame.pack_propagate(False)

    diagram_frame = Frame(middle_panel, width=round(middle_panel_width*0.455), height=middle_panel_height, bg='blue')
    diagram_frame.pack(side='right', fill=BOTH)
    diagram_frame.pack_propagate(False)

    left_button_panel = Frame(middle_panel, width=round(middle_panel_width*0.05), height=middle_panel_height, bg='green')
    left_button_panel.pack(side='right', fill=BOTH)
    left_button_panel.pack_propagate(False)

    income_button = Button(left_button_panel, text='Доход')
    income_button.grid(row=2, column=0, sticky='nsew')
    expenses_button = Button(left_button_panel, text='Расход')
    expenses_button.grid(row=3, column=0, sticky='nsew')
    year_button = Button(left_button_panel, text='?')
    year_button.grid(row=4, column=0, sticky='nsew')

    for i in range(7):
        left_button_panel.grid_rowconfigure(i, weight=1)


def open_expense_window():
    """
    Открывает окно для создания транзакции
    """

    global root

    def expense_submit():
        """
        Собирает данные для записи транзакции и закрывает окно
        """

        name = f_name_expense.get()
        amount = float(f_amount.get())
        payment_date = f_date.get()
        category = f_category.get()
        main(name, category, amount)
        spending_window.destroy()

    spending_window = Toplevel(root)
    spending_window.title("Window 1")
    spending_window.geometry("600x400")
    spending_window.attributes('-topmost', True)
    spending_window.lift()
    spending_window.focus_force()

    expense_categories = Category().category_list
    l_name_expense = Label(spending_window, text='На что потратил?')
    f_name_expense = Entry(spending_window, justify=RIGHT)
    l_category = Label(spending_window, text='Выбери категорию раcходов')
    f_category = Combobox(spending_window, values=expense_categories)
    l_amount = Label(spending_window, text='Введи сумму')
    f_amount = Entry(spending_window, justify=RIGHT)
    l_date = Label(spending_window, text='Введи дату')
    f_date = DateEntry(spending_window, date_pattern='dd-mm-YYYY')
    btn_submit = Button(spending_window, text="Submit", command=expense_submit)

    l_name_expense.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    f_name_expense.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    l_category.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    f_category.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    l_amount.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    f_amount.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    l_date.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    f_date.grid(row=3, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=4, column=0, columnspan=2)


def read_file():
    """
    Функция для формирования строк для холста с суммой расходов
    """

    global expense_file_path
    flist = summarize_expenses(expense_file_path)
    rows = ''
    for dic in flist:
        key = list(dic.keys())[0]
        meaning = sum(dic.get(key))
        rows += f'{key}: {meaning}\n'
    return rows


def open_menu():
    """
    Функция открывает боковое меню
    """

    def close_menu():
        canvas1.destroy()
        canvas2.destroy()

    canvas1 = Canvas(root, width=int(root.winfo_width() / 4), height=root.winfo_height(),
                     bg="red", highlightthickness=0)
    canvas1.pack_propagate(False)
    canvas1.place(x=0, y=0)

    empty_frame = Frame(canvas1, bg='white', width=int(root_width / 4), height=int(root_height * 0.2))
    empty_frame.pack_propagate(False)
    empty_frame.pack(side='top')

    button_2 = Button(canvas1, text="Счета", width=int(root_width / 8), height=int(root_height * 0.005))
    button_2.pack(side="top")

    button_3 = Button(canvas1, text="Категории", width=int(root_width / 8), height=int(root_height * 0.005))
    button_3.pack(side="top")

    button_4 = Button(canvas1, text="Напоминания", width=int(root_width / 8), height=int(root_height * 0.005))
    button_4.pack(side="top")

    button_5 = Button(canvas1, text="Заметки", width=int(root_width / 8), height=int(root_height * 0.005))
    button_5.pack(side="top")

    button_6 = Button(canvas1, text="Настройка профиля", width=int(root_width / 8), height=int(root_height * 0.005))
    button_6.pack(side="top")

    button_close_canvas = Button(canvas1, text="Close Canvas", command=close_menu, width=int(root_width / 8),
                                 height=int(root_height * 0.005))
    button_close_canvas.pack(side="top")

    canvas2 = Canvas(root, width=int(root.winfo_width() * 3 / 4), height=root.winfo_height(),
                     highlightthickness=0)
    canvas2.pack_propagate(False)
    canvas2.place(x=root.winfo_width() / 4, y=0)


create_top_panel()
create_middle_panel()

root.mainloop()
