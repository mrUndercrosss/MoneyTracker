from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from DB import WorkWithBD
from Categories import *
from ExpenseTracking import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime

from IncomeTracking import get_incomes_from_file


def open_menu(user):
    """
    Функция открывает боковое меню
    :param user: Объект TK
    """
    main_window = user.main_window
    list_of_canvas = []

    def categories():
        canvas_categories = open_categories(user)

    def close_menu():
        for canv in list_of_canvas:
            canv.destroy()

    root = main_window
    root_width = main_window.screen_width
    root_height = main_window.screen_height
    canvas_menu_main = Canvas(root, width=int(root_width / 4), height=root_height,
                              bg="red", highlightthickness=0)
    list_of_canvas.append(canvas_menu_main)
    canvas_menu_main.pack_propagate(False)
    canvas_menu_main.place(x=0, y=0)
    empty_frame = Frame(canvas_menu_main, bg='white', width=int(root_width / 4), height=int(root_height * 0.2))
    empty_frame.pack_propagate(False)
    empty_frame.pack(side='top')
    button_2 = Button(canvas_menu_main, text="Счета", width=int(root_width / 8), height=int(root_height * 0.005))
    button_2.pack(side="top")
    button_3 = Button(canvas_menu_main, text="Категории", width=int(root_width / 8), height=int(root_height * 0.005),
                      command=categories)
    button_3.pack(side="top")
    button_4 = Button(canvas_menu_main, text="Напоминания", width=int(root_width / 8), height=int(root_height * 0.005))
    button_4.pack(side="top")
    button_5 = Button(canvas_menu_main, text="Заметки", width=int(root_width / 8), height=int(root_height * 0.005))
    button_5.pack(side="top")
    button_6 = Button(canvas_menu_main, text="Настройка профиля", width=int(root_width / 8),
                      height=int(root_height * 0.005))
    button_6.pack(side="top")
    button_close_canvas = Button(canvas_menu_main, text="Close Canvas", command=close_menu, width=int(root_width / 8),
                                 height=int(root_height * 0.005))
    button_close_canvas.pack(side="top")
    canvas_menu_additional = Canvas(root, width=int(root_width * 3 / 4), height=root_height,
                                    highlightthickness=0)
    list_of_canvas.append(canvas_menu_additional)
    canvas_menu_additional.pack_propagate(False)
    canvas_menu_additional.place(x=root_width / 4, y=0)

    def open_categories(user):

        main_window = user.main_window
        expence_category = ExpenseCategories()
        income_category = IncomeCategories()

        def change_category_type():

            if user.expenses_or_income == 'e':
                user.expenses_or_income = 'i'
            else:
                user.expenses_or_income = 'e'
            canvas_categories.destroy()
            open_categories(user)

        def new_category():
            add_category_canvas = open_new_category()

        def fill_out_canvas():
            """
            Функция очищает canvas_categories и заполняет соответствующими категориями
            """
            if user.expenses_or_income == 'e':
                category_dict = expence_category.category_dict.keys()
            else:
                category_dict = income_category.category_dict.keys()

            for categor in list(category_dict):
                categories_label = Label(canvas_categories, text=categor, width=round(root_width * 0.05),
                                         height=round(root_height * 0.005), background='blue')
                categories_label.pack(side='top')

        def open_new_category():

            colors_values = ['red', 'blue', 'purple', 'brown', 'yellow']

            def category_submit():

                name = name_entry.get()
                image = image_entry.get()
                comment = comment_entry.get()
                color = color_entry.get()
                if name:
                    if user.expenses_or_income == 'e':
                        expence_category.add_category(name, color, user.expenses_or_income)
                    else:
                        income_category.add_category(name, color, user.expenses_or_income)
                add_category_canvas.destroy()
                canvas_categories.destroy()
                categories()

            add_category_canvas = Canvas(root, width=int(root_width * 3 / 4), height=root_height, highlightthickness=0)
            list_of_canvas.append(add_category_canvas)
            add_category_canvas.pack_propagate(False)
            add_category_canvas.place(x=root_width / 4, y=0)
            name_label = Label(add_category_canvas, text="Введите название")
            name_entry = Entry(add_category_canvas, justify=RIGHT)
            image_label = Label(add_category_canvas, text="Введите картинку")
            image_entry = Entry(add_category_canvas, justify=RIGHT)
            comment_label = Label(add_category_canvas, text="Введите комментарий")
            comment_entry = Entry(add_category_canvas, justify=RIGHT)
            color_label = Label(add_category_canvas, text='Выберите цвет для категории')
            color_entry = Combobox(add_category_canvas, values=colors_values)
            btn_submit = Button(add_category_canvas, text="Submit", command=category_submit)
            name_label.pack(side='top')
            name_entry.pack(side='top')
            image_label.pack(side='top')
            image_entry.pack(side='top')
            comment_label.pack(side='top')
            comment_entry.pack(side='top')
            color_label.pack(side='top')
            color_entry.pack(side='top')
            btn_submit.pack(side='top')
            return add_category_canvas

        root_width = main_window.screen_width
        root_height = main_window.screen_height
        canvas_menu_additional.destroy()
        canvas_categories = Canvas(main_window, width=int(root_width * 3 / 4), height=root_height, highlightthickness=0)
        list_of_canvas.append(canvas_categories)
        canvas_categories.pack_propagate(False)
        canvas_categories.place(x=root_width / 4, y=0)
        info_frame = Frame(canvas_categories, width=root_width, height=round(root_height * 0.1), bg='red')
        info_frame.pack_propagate(False)
        info_second_frame = Frame(canvas_categories, width=root_width, height=round(root_height * 0.1), bg='red')
        info_second_frame.pack_propagate(False)

        text_for_button = lambda x = user.expenses_or_income: 'Категория расходов' if x == 'e' else 'Категория доходов'
        change_category_type_button = Button(info_frame, text=text_for_button(), command=change_category_type)
        add_category_button = Button(info_second_frame, text='Добавить категорию', command=new_category)

        info_frame.pack(side='top')
        info_second_frame.pack(side='bottom')
        add_category_button.pack(side='top')
        change_category_type_button.pack(side='bottom')

        fill_out_canvas()
        return canvas_categories


def open_authorization(user):
    """
    Функция открывает меню авторизации
    :param user: Объект TK
    """
    main_window = user.main_window

    def authorization_submit():
        """
        Собирает данные для записи транзакции и закрывает окно
        """
        db = WorkWithBD()
        login = login_entry.get()
        password = password_entry.get()
        uid = db.to_authorization(login, password)
        if uid:
            user.user_id = uid
        canvas1.destroy()

    def close_authorization():
        canvas1.destroy()

    root = main_window
    root_width = main_window.screen_width
    root_height = main_window.screen_height

    def registrate():
        """
        Закрываем окно авторизации - открываем регистрации
        """
        close_authorization()
        open_registration(user)

    canvas1 = Canvas(root, width=root_width, height=root_height, highlightthickness=0)
    canvas1.pack_propagate(False)
    canvas1.place(x=0, y=0)
    authorization_label = Label(canvas1, text="Авторизация")
    authorization_label.pack(side='top')
    button_close_canvas = Button(canvas1, text="Close authorization", command=close_authorization,
                                 width=int(root_width / 6),
                                 height=int(root_height * 0.005))
    button_close_canvas.pack(side="bottom")
    help_frame = Frame(canvas1, width=int(root_width / 2), height=int(root_height / 2), bg='red')
    help_frame.pack_propagate(False)
    help_frame.pack(side="bottom")
    login_label = Label(help_frame, text="Введите логин")
    login_entry = Entry(help_frame, justify=RIGHT)
    password_label = Label(help_frame, text="Введите пароль")
    password_entry = Entry(help_frame, justify=RIGHT)
    btn_submit = Button(help_frame, text="Submit", command=authorization_submit)
    btn_registrate = Button(help_frame, text='Зарегестрироваться', command=registrate)
    login_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    login_entry.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    password_label.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    password_entry.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=4, column=0, columnspan=2)
    btn_registrate.grid(row=5, column=0, columnspan=2)


def open_registration(user):
    """
    :param user: Объект TK
    :return: Открывает окно регистрации
    """

    def close_register():
        canvas1.destroy()

    def registration_submit():
        """
        Собирает данные для записи транзакции и закрывает окно
        """
        db = WorkWithBD()
        name = name_entry.get()
        login = login_entry.get()
        password = password_entry.get()
        db.to_registrate(login, password)
        canvas1.destroy()

    def registrate():
        """
        Закрываем окно регистрации - открываем авторизации
        """
        close_register()
        open_authorization(user)

    main_window = user.main_window
    root = main_window
    root_width = main_window.screen_width
    root_height = main_window.screen_height
    canvas1 = Canvas(root, width=root_width, height=root_height, highlightthickness=0)
    canvas1.pack_propagate(False)
    canvas1.place(x=0, y=0)
    button_close_canvas = Button(canvas1, text="Close register", command=close_register, width=int(root_width / 6),
                                 height=int(root_height * 0.005))
    button_close_canvas.pack(side="bottom")
    registr_label = Label(canvas1, text="Регистрация")
    registr_label.pack(side='top')
    help_frame = Frame(canvas1, width=int(root_width / 2), height=int(root_height / 2), bg='red')
    help_frame.pack_propagate(False)
    help_frame.pack(side="bottom")
    name_label = Label(help_frame, text="Введите имя")
    name_entry = Entry(help_frame, justify=RIGHT)
    login_label = Label(help_frame, text="Введите логин")
    login_entry = Entry(help_frame, justify=RIGHT)
    password_label = Label(help_frame, text="Введите пароль")
    password_entry = Entry(help_frame, justify=RIGHT)
    btn_submit = Button(help_frame, text="Submit", command=registration_submit)
    btn_authorization = Button(help_frame, text='Авторизоваться', command=registrate)
    name_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    name_entry.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    login_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    login_entry.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    password_label.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    password_entry.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=4, column=0, columnspan=2)
    btn_authorization.grid(row=5, column=0, columnspan=2)


def open_expense_window(user):
    """
    Открывает окно для создания транзакции
    """

    def expense_submit():
        """
        Собирает данные для записи транзакции и закрывает окно
        """

        name = f_name_expense.get()
        amount = float(f_amount.get())
        payment_date = f_date.get()
        category = f_category.get()
        write_expenses(name=name, category=category, amount=round(amount), user_id=user.user_id, date=payment_date)
        upgrade_diagram_frame(user)
        spending_window.destroy()

    root = user.main_window

    spending_window = Toplevel(root)
    spending_window.title("Window 1")
    spending_window.geometry("350x250")
    spending_window.attributes('-topmost', True)
    spending_window.lift()
    spending_window.focus_force()
    spending_window.resizable(width=False, height=False)

    expense_categories = list(Category().get_expence_category_dict().keys())
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

def switch_diagram_type_to_income(user):
    user.expenses_or_income ='i'
    upgrade_diagram_frame(user)

def switch_diagram_type_to_expense(user):
    user.expenses_or_income ='e'
    upgrade_diagram_frame(user)

def get_graphic(Middle_panel, user=None):

    """
    Функция выводит диаграмму расходов/доходов за указанный период
    :param user:
    :return:
    """

    # if user.user_id:
    #     rows = db.get_expenses_from_db()
    # else:
    rows = [] # todo: Что должно быть на главном экране, если расходов нет?
    expense_file_path = "csv/expenses.csv"

    if expense_file_path:
        cat = ExpenseCategories()
        categories = cat.get_expence_category_dict()
        rows = get_expesnses_from_file(expense_file_path)

    if user:
        if user.expenses_or_income == 'i':
            income_file_path = "csv/incomes.csv"
            if income_file_path:
                cat = IncomeCategories()
                categories = cat.get_income_category_dict()
                rows = get_incomes_from_file(income_file_path)

    categories_in_diagram = []
    colors = []
    amount = []

    if rows:
        for row in rows:
            category_name, category_amount, category_date = row[-1], int(row[2]), row[-2]
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

    get_graphic(user.main_window.middle_panel, user)


def get_period_day(user):
    today = datetime.datetime.today()
    year, month, day = today.year, today.month, today.day
    date_today = f'{day}-{month}-{year}'
    user.main_window.middle_panel.period_date = [date_today]
    print(user.main_window.middle_panel.period_date)


def get_period_week(user):
    current_date = datetime.datetime.now()
    weekdays = []
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
    for i in range(7):
        date = start_of_week + datetime.timedelta(days=i)
        weekdays.append(date.strftime('%d-%m-%Y'))

    user.main_window.middle_panel.period_date = weekdays
    print(user.main_window.middle_panel.period_date)


def get_month(user):
    today = datetime.datetime.now()
    month = [f'{today.month}-{today.year}']
    user.main_window.middle_panel.period_date = month
    print(user.main_window.middle_panel.period_date)


def get_year(user):
    today = datetime.datetime.now()
    year = [f'{today.year}']
    user.main_window.middle_panel.period_date = year
    print(user.main_window.middle_panel.period_date)
