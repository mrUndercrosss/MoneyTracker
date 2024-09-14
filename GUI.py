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
    """Функция создает верхнюю панель, которая содержит кнопку вызова меню,
    кнопку авторизации и название счета вместе с периодом"""
    top_panel_frame = Frame(root, width=root_width, height=root_height * 0.1, highlightthickness=0)
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


def open_modal_window():
    global root

    def expense_submit():
        name = f_name_expense.get()
        amount = float(f_amount.get())
        payment_date = f_date.get()
        category = f_category.get()
        main(name, category, amount)
        window1.destroy()

    window1 = Toplevel(root)
    window1.title("Window 1")
    window1.geometry("600x400")
    window1.attributes('-topmost', True)
    window1.lift()
    window1.focus_force()

    expense_categories = Category().category_list
    l_name_expense = Label(window1, text='На что потратил?')
    f_name_expense = Entry(window1, justify=RIGHT)
    l_category = Label(window1, text='Выбери категорию раcходов')
    f_category = Combobox(window1, values=expense_categories)
    l_amount = Label(window1, text='Введи сумму')
    f_amount = Entry(window1, justify=RIGHT)
    l_date = Label(window1, text='Введи дату')
    f_date = DateEntry(window1, date_pattern='dd-mm-YYYY')
    btn_submit = Button(window1, text="Submit", command=expense_submit)

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
    :return:
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
    global is_purple
    global canvas1, canvas2
    canvas1 = Canvas(root, width=int(root.winfo_width() / 4), height=root.winfo_height(),
                         bg="red", highlightthickness=0)
    canvas1.pack_propagate(False)
    canvas1.place(x=0, y=0)

    empty_frame = Frame(canvas1, bg='white', width=int(root_width / 4), height=int(root_height * 0.2))
    empty_frame.pack_propagate(False)
    empty_frame.pack(side='top')

    button_close_canvas = Button(canvas1, text="Close Canvas", command=close_canvas, width=int(root_width / 8),
                                 height=int(root_height * 0.005))
    button_close_canvas.pack(side="top")

    button_2 = Button(canvas1, text="2", width=int(root_width / 8), height=int(root_height * 0.005))
    button_2.pack(side="top")

    button_3 = Button(canvas1, text="3", width=int(root_width / 8), height=int(root_height * 0.005))
    button_3.pack(side="top")

    button_4 = Button(canvas1, text="4", width=int(root_width / 8), height=int(root_height * 0.005))
    button_4.pack(side="top")

    button_5 = Button(canvas1, text="5", width=int(root_width / 8), height=int(root_height * 0.005))
    button_5.pack(side="top")

    button_6 = Button(canvas1, text="6", width=int(root_width / 8), height=int(root_height * 0.005))
    button_6.pack(side="top")

    button_change_color = Button(canvas1, text="Change Background Color", command=change_background_color,
                                 width=int(root_width / 8), height=int(root_height * 0.005))
    button_change_color.pack(side="top")

    canvas2 = Canvas(root, width=int(root.winfo_width() * 3 / 4), height=root.winfo_height(),
                         highlightthickness=0)
    canvas2.pack_propagate(False)
    canvas2.place(x=root.winfo_width() / 4, y=0)


def close_canvas():
    global canvas1, canvas2
    canvas1.destroy()
    canvas2.destroy()


def change_background_color():
    global root
    global is_purple
    if is_purple:
        root.config(bg='green')
        is_purple = False
    else:
        root.config(bg='purple')
        is_purple = True


create_top_panel()
root.mainloop()
