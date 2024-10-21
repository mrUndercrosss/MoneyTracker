from tkinter import *
from DB import WorkWithBD
from Categories import Category


def open_menu(main_window):
    """
    Функция открывает боковое меню
    :param main_window: Объект TK
    """
    global list_of_canvas
    list_of_canvas = []  # todo: Подумать над реализацией списка канвасов для их закрытия
    global canvas_menu_main
    global canvas_menu_additional

    def categories():
        global canvas_categories
        canvas_categories = open_categories(main_window)
        list_of_canvas.append(canvas_categories)

    def close_menu():
        canvas_menu_main.destroy()
        canvas_menu_additional.destroy()
        canvas_categories.destroy()  # todo: Если 2 раза нажать на "Категории", то закроется только один канвас
        add_category_canvas.destroy()  # todo: Придумать как проверять, не используя его название

    root = main_window.main_windows
    root_width = main_window.screen_width
    root_height = main_window.screen_height
    canvas_menu_main = Canvas(root, width=int(root_width / 4), height=root_height,
                              bg="red", highlightthickness=0)
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
    canvas_menu_additional.pack_propagate(False)
    canvas_menu_additional.place(x=root_width / 4, y=0)

    def open_categories(main_window):
        category = Category()

        def new_category():
            global add_category_canvas
            add_category_canvas = open_new_category()

        def open_new_category():
            def category_submit():
                name = name_entry.get()
                image = image_entry.get()
                comment = comment_entry.get()
                category.add_category(name)
                add_category_canvas.destroy()
                canvas_categories.destroy()
                categories()

            add_category_canvas = Canvas(root, width=int(root_width * 3 / 4), height=root_height, highlightthickness=0)
            add_category_canvas.pack_propagate(False)
            add_category_canvas.place(x=root_width / 4, y=0)
            name_label = Label(add_category_canvas, text="Введите название")
            name_entry = Entry(add_category_canvas, justify=RIGHT)
            image_label = Label(add_category_canvas, text="Введите картинку")
            image_entry = Entry(add_category_canvas, justify=RIGHT)
            comment_label = Label(add_category_canvas, text="Введите комментарий")
            comment_entry = Entry(add_category_canvas, justify=RIGHT)
            btn_submit = Button(add_category_canvas, text="Submit", command=category_submit)
            name_label.pack(side='top')
            name_entry.pack(side='top')
            image_label.pack(side='top')
            image_entry.pack(side='top')
            comment_label.pack(side='top')
            comment_entry.pack(side='top')
            btn_submit.pack(side='top')
            return add_category_canvas

        root = main_window.main_windows
        root_width = main_window.screen_width
        root_height = main_window.screen_height
        canvas_menu_additional.destroy()
        canvas_categories = Canvas(root, width=int(root_width * 3 / 4), height=root_height, highlightthickness=0)
        canvas_categories.pack_propagate(False)
        canvas_categories.place(x=root_width / 4, y=0)
        info_frame = Frame(canvas_categories, width=root_width, height=round(root_height * 0.1), bg='red')
        info_frame.pack_propagate(False)
        info_second_frame = Frame(canvas_categories, width=root_width, height=round(root_height * 0.1), bg='red')
        info_second_frame.pack_propagate(False)
        add_category_button = Button(info_second_frame, text='Добавить категорию', command=new_category)
        info_frame.pack(side='top')
        info_second_frame.pack(side='bottom')
        add_category_button.pack(side='top')
        for categor in category.category_list:
            categories_label = Label(canvas_categories, text=categor, width=round(root_width * 0.05),
                                     height=round(root_height * 0.005), background='blue')
            categories_label.pack(side='top')
        return canvas_categories


def open_authorization(main_window):
    """
    Функция открывает меню авторизации
    :param main_window: Объект TK
    """

    def authorization_submit():
        """
        Собирает данные для записи транзакции и закрывает окно
        """
        db = WorkWithBD()
        login = login_entry.get()
        password = password_entry.get()
        db.to_authorization(login, password)
        canvas1.destroy()

    def close_authorization():
        canvas1.destroy()

    root = main_window.main_windows
    root_width = main_window.screen_width
    root_height = main_window.screen_height

    def registrate():
        """
        Закрываем окно авторизации - открываем регистрации
        """
        close_authorization()
        open_registration(main_window)

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


def open_registration(main_window):
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
        db.to_registrate(23, login, password)
        canvas1.destroy()

    def registrate():
        """
        Закрываем окно регистрации - открываем авторизации
        """
        close_register()
        open_authorization(main_window)

    root = main_window.main_windows
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
