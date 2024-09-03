from tkinter import *
from ExpenseTracking import *
canvas_is_open = False
is_purple = True
expense_file_path = "csv/expenses.csv"
def open_modal_window(window_name):
    global root
    if window_name == "Window 1":
        window1 = Toplevel(root)
        window1.title("Window 1")
        window1.geometry("300x200")
        window1.attributes('-topmost', True)
        window1.lift()
        window1.focus_force()
    elif window_name == "Window 2":
        window2 = Toplevel(root)
        window2.title("Window 2")
        window2.geometry("300x200")
        window2.attributes('-topmost', True)
        window2.lift()
        window2.focus_force()
    elif window_name == "Window 3":
        window3 = Toplevel(root)
        window3.title("Window 3")
        window3.geometry("300x200")
        window3.attributes('-topmost', True)
        window3.lift()
        window3.focus_force()
    else:
        window4 = Toplevel(root)
        window4.title("Window 4")
        window4.geometry("300x200")
        window4.attributes('-topmost', True)
        window4.lift()
        window4.focus_force()
def read_file():
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
        canvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height(), bg="purple" if is_purple else "green", highlightthickness=0)
        canvas.pack(side="bottom")
        canvas_is_open = True
        canvas.create_rectangle(root.winfo_width()*0.25, root.winfo_height(), root.winfo_width()*0.75, 0, fill='red')
        canvas.create_text(root.winfo_width()*0.5, root.winfo_height()*0.25, text=f"{read_file()}", fill='white')
def close_canvas():
    global canvas
    global canvas_is_open
    canvas.destroy()
    canvas_is_open = False
def change_background_color():
    global root
    global is_purple
    global canvas
    if is_purple:
        root.config(bg='green')
        is_purple = False
    else:
        root.config(bg='purple')
        is_purple = True
root = Tk()
root.title("Main Window")
root.geometry("1200x900")
root.config(bg='Purple')
main_menu = Menu(root)
root.config(menu=main_menu)

frame = Frame(root)
frame.pack(side='bottom')


button1 = Button(frame, text="Change Background Color", command=change_background_color)
button1.pack(side="left")
button2 = Button(frame, text="Open Canvas", command=open_canvas)
button2.pack(side="left")
button3 = Button(frame, text="Close Canvas", command=close_canvas)
button3.pack(side="left")
button4 = Button(frame, text="Open Window 4", command=lambda: open_modal_window("Window 4"))
button4.pack(side="left")
button5 = Button(frame, text="Add expense", command=lambda: main())
button5.pack(side="left")
root.mainloop()