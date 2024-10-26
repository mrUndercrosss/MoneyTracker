from tkinter import *
from Function import *
from DB import *
from Person import Person, MainWindow


class Panel(Person):
    def __init__(self, width=100, height=100):
        super().__init__()
        self.side = None
        self.frame = None
        self.width = width
        self.height = height

    def attach_to(self, space, side: str, bg=None):
        """
        :param space:
        :param side:
        :param bg:
        :return:
        """
        self.frame = Frame(space, width=self.width, height=self.height, highlightthickness=0, bg=bg)
        self.frame.pack(side=side)
        self.frame.pack_propagate(False)
        return self

    def add_button(self, space, frame_side, button_side, width, height, w_divisor, h_divisor,
                   panel=None, command=None, bg=None, text='Кноп'):
        """
        :param panel:
        :param space:
        :param frame_side:
        :param button_side:
        :param width:
        :param height:
        :param w_divisor:
        :param h_divisor:
        :param bg:
        :param text:
        :return:
        """
        space_frame = Panel(round(self.width / w_divisor), round(self.height / h_divisor))
        space_frame = space_frame.attach_to(space, frame_side, bg=bg)
        button = Button(space_frame.frame, text=text, width=width, height=height, command=command)
        button.pack(side=button_side)
        return button


class TopPanel(Panel):
    def __init__(self, user):
        super().__init__()
        main_window = user.main_window
        self.width = main_window.screen_width
        self.height = round(main_window.screen_height * 0.1)
        self.attach_to(main_window, 'top')
        self.menu_frame = Panel(round(self.width / 3), self.height)
        self.menu_frame.attach_to(self.frame, 'left', 'green')
        self.menu_frame.add_button(self.menu_frame.frame, frame_side='left', button_side='right',
                                   width=int(self.width / 224),
                                   height=self.height, bg='green', w_divisor=6,
                                   h_divisor=1, command=self.menu)
        self.account_name_frame = Panel(round(self.width / 3), self.height)
        self.account_name_frame.attach_to(self.frame, 'left', 'red')
        self.authorization_frame = Panel(round(self.width / 3), self.height)
        self.authorization_frame.attach_to(self.frame, 'left', 'blue')
        self.authorization_frame.add_button(self.authorization_frame.frame, frame_side='right', button_side='left',
                                            width=int(self.width / 224), height=self.height,
                                            bg='blue', w_divisor=6, h_divisor=1, command=self.authorization)

    @staticmethod
    def menu():
        global user
        open_menu(user)

    @staticmethod
    def authorization():
        global user
        open_authorization(user)


class MiddlePanel(Panel):
    def __init__(self, user):
        super().__init__()
        main_window = user.main_window
        self.width = main_window.screen_width
        self.height = round(main_window.screen_height * 0.7)
        self.attach_to(main_window, side='top', bg='sky blue')
        self.right_button_panel = Panel(width=round(self.width * 0.05), height=self.height)
        self.right_button_panel.attach_to(self.frame, 'right', 'green')
        empty_space = Panel(width=round(self.width * 0.05), height=round(self.height / 7))
        empty_space.attach_to(self.right_button_panel.frame, 'top', 'green')

        day_button = self.right_button_panel.add_button(self.right_button_panel.frame, frame_side='top',
                                                        button_side='bottom',
                                                        width=int(self.width), height=self.height, bg='green',
                                                        w_divisor=1,
                                                        h_divisor=7, text='День')
        week_button = self.right_button_panel.add_button(self.right_button_panel.frame, frame_side='top',
                                                         button_side='bottom',
                                                         width=int(self.width), height=self.height, bg='green',
                                                         w_divisor=1,
                                                         h_divisor=7, text='Неделя')
        month_button = self.right_button_panel.add_button(self.right_button_panel.frame, frame_side='top',
                                                          button_side='bottom',
                                                          width=int(self.width), height=self.height, bg='green',
                                                          w_divisor=1,
                                                          h_divisor=7, text='Месяц')
        year_button = self.right_button_panel.add_button(self.right_button_panel.frame, frame_side='top',
                                                         button_side='bottom',
                                                         width=int(self.width), height=self.height, bg='green',
                                                         w_divisor=1,
                                                         h_divisor=7, text='Год')
        period_button = self.right_button_panel.add_button(self.right_button_panel.frame, frame_side='top',
                                                           button_side='bottom',
                                                           width=int(self.width), height=self.height, bg='green',
                                                           w_divisor=1, h_divisor=7, text='Период')
        self.graph_frame = Panel(width=round(self.width * 0.45), height=self.height)
        self.graph_frame.attach_to(self.frame, 'right', 'purple')
        self.diagram_frame = Panel(width=round(self.width * 0.45), height=self.height)
        self.diagram_frame.attach_to(self.frame, 'right', 'orange')
        self.left_button_panel = Panel(width=round(self.width * 0.05), height=self.height)
        self.left_button_panel.attach_to(self.frame, 'right', 'green')
        empty_space = Panel(width=round(self.width * 0.05), height=round(self.height * 2 / 7))
        empty_space.attach_to(self.left_button_panel.frame, 'top', 'green')
        income_button = self.left_button_panel.add_button(self.left_button_panel.frame, frame_side='top',
                                                          button_side='bottom',
                                                          width=int(self.width), height=self.height, bg='green',
                                                          w_divisor=1,
                                                          h_divisor=7, text='Доход')
        expenses_button = self.left_button_panel.add_button(self.left_button_panel.frame, frame_side='top',
                                                            button_side='bottom',
                                                            width=int(self.width), height=self.height, bg='green',
                                                            w_divisor=1,
                                                            h_divisor=7, text='Расход')
        year_button = self.left_button_panel.add_button(self.left_button_panel.frame, frame_side='top',
                                                        button_side='bottom',
                                                        width=int(self.width), height=self.height, bg='green',
                                                        w_divisor=1,
                                                        h_divisor=7, text='?')


class BottomPanel(Panel):

    def __init__(self, user):
        super().__init__()
        main_window = user.main_window
        self.width = main_window.screen_width
        self.height = round(main_window.screen_height * 0.2)
        self.bottom_panel = self.attach_to(main_window, side='top', bg='blue')

        self.add_button(self.bottom_panel.frame, frame_side='top',
                        button_side='top',
                        w_divisor=3,
                        h_divisor=5,
                        width=int(self.width), height=self.height, bg='green',
                        text='Добавить транзакцию', command=self.expense_window)

    @staticmethod
    def expense_window():
        global user
        open_expense_window(user)


user = Person()
user.main_window = MainWindow()

top_panel = TopPanel(user)
middle_panel = MiddlePanel(user)
bottom_panel = BottomPanel(user)

user.main_window.run()
