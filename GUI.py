from AuxiliaryFunctions import *

canvas_is_open = False
is_purple = True
expense_file_path = "csv/expenses.csv"


button1 = Button(frame, text="Change Background Color", command=change_background_color)
button1.pack(side="left")
button2 = Button(frame, text="Open Canvas", command=open_canvas)
button2.pack(side="left")
button3 = Button(frame, text="Close Canvas", command=close_canvas)
button3.pack(side="left")
button4 = Button(frame, text="Open Window 4", command=lambda: open_modal_window())
button4.pack(side="left")
button5 = Button(frame, text="Add expense", command=lambda: main())
button5.pack(side="left")



root.mainloop()
