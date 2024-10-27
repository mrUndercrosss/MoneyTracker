class Category:
    category_file = 'csv/Categories.csv'

    def get_expence_category_dict(self):
        category_dict = {}
        with open(self.category_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "\n" in line:
                    line = line[:-1]
                    if len(line) == 0:
                        continue
                key = line.split(':')[0]
                value = [line.split(':')[1]]
                category_dict[key] = value

        return category_dict

    def get_income_category_list(self):
        pass

    def add_category(self, new_category, color):
        with open(self.category_file, "a") as file:
            file.write(f"{new_category}:{color}\n")

    def __init__(self):
        self.color = None


class ExpenseCategories(Category):
    def __init__(self):
        super().__init__()
        self.category_dict = self.get_expence_category_dict()


class IncomeCategories(Category):
    def __init__(self):
        super().__init__()
        self.get_income_category_list()
