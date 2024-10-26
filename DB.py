import psycopg2
from psycopg2 import OperationalError
from Person import Person


class WorkWithBD(Person):

    def create_table_if_not_exist(self):
        query = f"""CREATE TABLE IF NOT EXISTS expenses (id INTEGER, name TEXT)
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

    def write_to_bd(self, name, category, amount, user_id, date):
        comment = 1
        query = """
                select id from expenses
                where user_id = %s
                order by id desc
                """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            id = result[0] + 1
        else:
            id = 1

        query = """
        INSERT INTO public.expensess(
	    id, "Transaction_name", "Transaction_category", "Value", "Comment", "Transaction_date", user_id)
	    VALUES (%s, %s, %s, %s, %s, %s);
        """
        print(f'User ID: {user_id}')
        self.cursor.execute(query, (id, name, category, amount, comment, user_id, date)) # TypeError: not all arguments converted during string formatting. Я рот того манал
        self.conn.commit()
        print('Записал в бд')

    def to_authorization(self, login, password):
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
            elif password == result[2] and login == result[1]:
                print('Логин удался')
                return result[0]
        else:
            print('Попробуй ещё раз')

    def get_user_expenses(self):
        query = """
                select *
                FROM expenses
                WHERE user_id = %s
                """
        self.cursor.execute(query, str(self.user_id))
        result = self.cursor.fetchall()
        print(result)

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
#
# create_expenses_main_table = f"""CREATE TABLE IF NOT EXISTS expenses(
#  id SERIAL PRIMARY KEY,
#  name_transaction TEXT,
#  value INT,
#  comment TEXT,
#  user_id INTEGER REFERENCES users(user_id)
# )
# """
#
# user = WorkWithBD()
# user.to_register('4', 'Myster_J', 'Xx123')
# user.to_authorization('mr_Oleg', 'Not_password')
# connection.get_user_expenses()
# print()
