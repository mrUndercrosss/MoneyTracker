class Expense:

    def __init__(self, name, category, amount, date, user_id) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.user_id = user_id
        self.date = date


    def generate_json(self):
        record = f'name:{self.name}|category:{self.category}|amount:{self.amount}|user_id:{self.user_id}|date:{self.date}\n'
        return record

