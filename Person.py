from tkinter import *


class Person:

    def __init__(self):
        self.user_id = None
        self.login = None
        self.additional_info = None
        self.main_window = None
        self.expenses_or_income = 'e'


class MainWindow(Tk):
    def __init__(self, color='Purple'):
        super().__init__()
        self.screen_width = int(self.winfo_screenwidth() * 0.75)
        self.screen_height = int(self.winfo_screenheight() * 0.75)
        self.geometry(f"{self.screen_width}x{self.screen_height}")
        self.config(bg=color)
        self.resizable(width=False, height=False)
        self.top_panel = None
        self.middle_panel = None
        self.bottom_panel = None

    def run(self):
        self.mainloop()
