# -*- coding: cp1251 -*-
import psycopg2
from psycopg2 import OperationalError

from IncomeTracking import write_to_file as write_income, get_incomes_from_file, clear_income_file
from ExpenseTracking import write_to_file as write_expense, get_expesnses_from_file, clear_expense_file
from Person import Person
from Categories import Category


class WorkWithBD(Person):

    def create_table_if_not_exist(self):
        query = f"""CREATE TABLE IF NOT EXISTS categories (user_id INTEGER, category_name TEXT, color TEXT, type TEXT)
                    """
        self.cursor.execute(query)
        self.conn.commit()

    def __init__(self):
        super().__init__()
        self.db_uri = 'postgresql://testuser:mr_undercross48162@localhost:5432/MoneyTracker'
        self.conn = psycopg2.connect(self.db_uri)
        self.cursor = self.conn.cursor()

    def to_registrate(self, login, password):

        query = """
        SELECT user_id
        FROM users
        order by user_id desc
        """
        self.cursor.execute(query, (login,))
        user_id = self.cursor.fetchone()
        user_id = user_id[0] + 1

        query = """
        INSERT INTO public.users(
	    user_id, login, password)
	    VALUES (%s, %s, %s); 
        """

        self.cursor.execute(query, (user_id, login, password))
        self.conn.commit()
        self.insert_standart_pack(user_id)

    def write_categories_to_bd(self, user_id, category_name, color, type):
        query = """
                INSERT INTO public.categories (user_id, category_name, color, type)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id, category_name, type) DO UPDATE
                SET color = EXCLUDED.color
                """
        self.cursor.execute(query, (user_id, category_name, color, type))
        self.conn.commit()

    def write_to_bd(self, name, category, amount, user_id, date, tranzaction_type):

        tranzaction_type = 'expenses' if tranzaction_type == 'e' else 'incomes'
        comment = ''
        query = f"""
                select id from {tranzaction_type}
                order by id desc
                """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            id = result[0] + 1
        else:
            id = 1

        query = f"""
        INSERT INTO public.{tranzaction_type}
        (id, name_transaction, value, comment, user_id, transaction_date, category)
	    VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        print(f'User ID: {user_id}')
        self.cursor.execute(query, (id, name, amount, comment, user_id, date, category))
        self.conn.commit()
        print('Записал в бд')

    def try_login(self, login: str, password: str):
        query = """
        SELECT *
        FROM USERS
        WHERE login = %s
        """
        self.cursor.execute(query, (login,))
        result = self.cursor.fetchone()

        if result:
            if password != result[2]:
                print('Не угадал')
                return False, None
            elif password == result[2] and login == result[1]:
                print('Логин удался')
                return True, result[0]
        else:
            print('Попробуй ещё раз')
            return False, None

    def to_authorization(self, login, password):
        result, user_id = self.try_login(login=login, password=password)
        if result:
            self.check_files(user_id=user_id)
            self.get_info(user_id=user_id)

    def check_files(self, user_id):
        self.check_expenses(user_id=user_id)
        self.check_incomes(user_id=user_id)
        self.check_categories(user_id=user_id)

    def check_categories(self, user_id):
        result = Category.get_all_categories()
        if result:
            for row in result:
                self.write_categories_to_bd(user_id=user_id,
                                            category_name=row.get('category_name'),
                                            color=row.get('category_color'),
                                            type=row.get('category_type')
                                            )
            Category.clear_category_file()

    def check_incomes(self, user_id):
        result = get_incomes_from_file()
        if result:
            for row in result:
                self.write_to_bd(name=row.get('income_name'),
                                 category=row.get('income_category'),
                                 amount=row.get('income_amount'),
                                 user_id=user_id,
                                 date=row.get('income_date'),
                                 tranzaction_type='i')
            clear_income_file()

    def check_expenses(self, user_id):
        result = get_expesnses_from_file()
        if result:
            for row in result:
                self.write_to_bd(name=row.get('expense_name'),
                                 category=row.get('expense_category'),
                                 amount=row.get('expense_amount'),
                                 user_id=user_id,
                                 date=row.get('expense_date'),
                                 tranzaction_type='e')
            clear_expense_file()

    def get_info(self, user_id):
        self.get_expenses_from_db(user_id=user_id)
        print()
        self.get_incomes_from_db(user_id=user_id)
        self.get_category_from_db(user_id=user_id)

    def get_category_from_db(self, user_id):
        query = """
                        select *
                        FROM categories
                        WHERE user_id = %s
                        """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchall()
        if result:
            for category in result:
                Category.add_category(new_category=category[1],
                                      color=category[2],
                                      category_type=category[3])
        return result

    def get_incomes_from_db(self, user_id):
        query = """
                select *
                FROM incomes
                WHERE user_id = %s
                """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchall()
        if result:
            for transaction in result:
                write_income(name=transaction[1],
                             category=transaction[6],
                             amount=transaction[2],
                             user_id=transaction[4],
                             date=transaction[5])
        return result

    def get_expenses_from_db(self, user_id):
        query = """
                select *
                FROM expenses
                WHERE user_id = %s
                """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchall()
        if result:
            for transaction in result:
                write_expense(name=transaction[1],
                              category=transaction[6],
                              amount=transaction[2],
                              user_id=transaction[4],
                              date=transaction[5])

        return result

    def insert_standart_pack(self, user_id):
        query = """
        INSERT INTO public.categories(
	    user_id, category_name, color, type)
	    VALUES (%s, %s, %s, %s);
        """
        standart_pack = [
            ['Досуг', 'yellow', 'e'],
            ['Прочее', 'blue', 'e'],
            ['Транспорт', 'red', 'e'],
            ['Здоровье', 'brown', 'e'],
            ['Разврат', 'red', 'e'],
            ['Мечта', 'blue', 'e'],
            ['Зарплата', 'green', 'i'],
            ['Подарили', 'blue', 'i'],
            ['Взятки', 'red', 'i'],
            ['Снюс', 'brown', 'e'],
            ['Ещё одна', 'purple', 'e'],
            ['Проценты с инвестиций', 'purple', 'e'],
        ]
        for category in standart_pack:
            self.cursor.execute(query, (user_id, category[0], category[1], category[2]))
            self.conn.commit()

    # finally:
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()
    #
    # def execute_query(self, query):
    #     self.conn.autocommit = True
    #     cursor = self.conn.cursor()
    #     try:
    #         cursor.execute(query)
    #         print("Query executed successfully")
    #     except OperationalError as e:
    #         print(f"The error '{e}' occurred")
    #
    # create_users_table = """
    # CREATE TABLE IF NOT EXISTS users (
    #   user_id SERIAL PRIMARY KEY,
    #   login TEXT NOT NULL,
    #   password TEXT NOT NULL
    # )
    # """
    #
    # create_posts_table = """
    # CREATE TABLE IF NOT EXISTS additional_info (
    #   id SERIAL PRIMARY KEY,
    #   Name TEXT,
    #   Surname TEXT,
    #   Sex TEXT,
    #   One TEXT,
    #   Two TEXT,
    #   Three TEXT,
    #   Four TEXT,
    #   user_id INTEGER REFERENCES users(user_id)
    # )
    # """

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS incomes(
         id SERIAL PRIMARY KEY,
         name_transaction TEXT,
         value INT,
         comment TEXT,
         user_id INTEGER REFERENCES users(user_id),
         transaction_date TEXT,
         category TEXT
        )
         """

        self.cursor.execute(query)
        self.conn.commit()


#
# user = WorkWithBD()
# user.to_authorization(login='1', password='1')
# print()
# user.to_register('4', 'Myster_J', 'Xx123')
# user.to_authorization('mr_Oleg', 'Not_password')
# connection.get_user_expenses()
# print()
