from tkinter import *
from tkinter.ttk import Combobox
from ExpenseTracking import *
from Categories import *
from tkcalendar import DateEntry, Calendar

canvas_is_open = False
is_purple = True
expense_file_path = "csv/expenses.csv"

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Main Window")
root.geometry(f"{int(screen_width * 0.75)}x{int(screen_height * 0.75)}")
root.config(bg='Purple')

frame = Frame(root)
frame.pack(side='bottom')
frame.config(bg='Purple')


def open_modal_window():
    global root

    window1 = Toplevel(root)
    window1.title("Window 1")
    window1.geometry("600x400")
    window1.attributes('-topmost', True)
    window1.lift()
    window1.focus_force()

    expense_categories = Category().category_list
    l_choose = Label(window1, text='Выберите категорию раcходов')
    f_choose = Combobox(window1, values=expense_categories)
    l_amount = Label(window1, text='Введите сумму')
    f_amount = Entry(window1, justify=RIGHT)
    l_date = Label(window1, text='Введите дату')
    f_date = DateEntry(window1, date_pattern='dd-mm-YYYY')
    btn_submit = Button(window1, text="Submit", command=main())

    l_choose.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    f_choose.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    l_amount.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    f_amount.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    l_date.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    f_date.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=3, column=0, columnspan=2)


def read_file():
    """

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


def open_canvas():
    global is_purple
    global canvas_is_open
    global canvas
    if not canvas_is_open:
        canvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height(),
                        bg="purple" if is_purple else "green", highlightthickness=0)
        canvas.pack(side="bottom")
        canvas_is_open = True
        canvas.create_rectangle(root.winfo_width() * 0.25, root.winfo_height(), root.winfo_width() * 0.75, 0,
                                fill='red')
        canvas.create_text(root.winfo_width() * 0.5, root.winfo_height() * 0.25, text=f"{read_file()}", fill='white')


def close_canvas():
    global canvas
    global canvas_is_open
    canvas.destroy()
    canvas_is_open = False


def change_background_color():
    global root
    global is_purple
    global canvas
    global frame
    if is_purple:
        root.config(bg='green')
        frame.config(bg='green')
        is_purple = False
    else:
        root.config(bg='purple')
        frame.config(bg='purple')
        is_purple = True

