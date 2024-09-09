from tkinter import *

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# window.wm_attributes('-alpha', 0.8)
window.title('Мяу')
window.geometry(f"{int(screen_width * 0.75)}x{int(screen_height * 0.75)}")
# window.resizable(width=False, height=False)
print(window.winfo_screenwidth())
print(window.winfo_screenheight())
frame_width = int(window.winfo_screenwidth()*0.75*0.5)
frame_height = int(window.winfo_screenheight()*0.75*0.75)
frame_blue_width = 2 * frame_width

frame_green = Frame(window, bg='green', width=frame_width, height=frame_height)
frame_yellow = Frame(window, bg='yellow', width=frame_width, height=frame_height)
frame_blue = Frame(window, bg='blue', width=frame_blue_width, height=window.winfo_screenheight() - frame_height)

frame_green.grid(column=0, row=0, sticky='nsew')
frame_yellow.grid(column=1, row=0, sticky='nsew')
frame_blue.grid(column=0, row=1, columnspan=2, sticky='nsew')

help_green_frame1 = Frame(frame_green, width=frame_width, height=int(frame_height/5))
help_green_frame1.pack(side="bottom")
help_green_frame1.configure(bg='red')
help_green_frame1.pack_propagate(False)

help_green_frame2 = Frame(frame_green, width=frame_width, height=int(frame_height/5))
help_green_frame2.pack(side="bottom")
help_green_frame2.configure(bg='black')
help_green_frame3 = Frame(frame_green, width=frame_width, height=int(frame_height/5))
help_green_frame3.pack(side="bottom")
help_green_frame3.configure(bg='blue')
help_green_frame4 = Frame(frame_green, width=frame_width, height=int(frame_height/5))
help_green_frame4.pack(side="bottom")
help_green_frame4.configure(bg='orange')
help_green_frame5 = Frame(frame_green, width=frame_width, height=int(frame_height/5))
help_green_frame5.pack(side="bottom")
help_green_frame5.configure(bg='purple')

help_yellow_frame1 = Frame(frame_yellow, width=frame_width, height=int(frame_height/5))
help_yellow_frame1.pack(side="left")
# help_yellow_frame2 = Frame(frame_yellow, width=frame_width, height=int(frame_height/5))
# help_yellow_frame2.pack(side="top")
# help_yellow_frame3 = Frame(frame_yellow, width=frame_width, height=int(frame_height/5))
# help_yellow_frame3.pack(side="top")
# help_yellow_frame4 = Frame(frame_yellow, width=frame_width, height=int(frame_height/5))
# help_yellow_frame4.pack(side="top")


label = Label(help_green_frame1, text="Sample Text", fg="white", bg="black")
label.pack()
# button1 = Button(help_green_frame1, text="Button1")
# button1.pack(side='left')
# button2 = Button(help_green_frame1, text="Button1")
# button2.pack(side='left')
# l1 = Label(help_green_frame1, text='Label1')
# l1.pack(side='left')
# l2 = Label(help_green_frame1, text='Label2')
# l2.pack(side='right')
# l3 = Label(help_green_frame3, text='Label3')
# l3.pack(side='left')
# l4 = Label(help_green_frame4, text='Label4')
# l4.pack(side='right')


window.mainloop()
