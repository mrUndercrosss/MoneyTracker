class Category:
    category_file = 'csv/Categories.csv'

    def __init__(self):
        self.color = None

    def get_expense_category_dict(self):
        category_dict = {}
        with open(self.category_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "\n" in line:
                    line = line[:-1]
                    if len(line) == 0:
                        continue
                key = line.split(':')[0]
                value = line.split(':')[1][:-2].strip()
                category_type = line.split(':')[1][-1].strip()
                if category_type == 'e':
                    category_dict[key] = [value, category_type]

        return category_dict

    def get_income_category_dict(self):
        category_dict = {}
        with open(self.category_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "\n" in line:
                    line = line[:-1]
                    if len(line) == 0:
                        continue
                key = line.split(':')[0]
                value = line.split(':')[1][:-2].strip()
                category_type = line.split(':')[1][-1].strip()
                if category_type == 'i':
                    category_dict[key] = [value, category_type]

        return category_dict

    @staticmethod
    def add_category(new_category, color, category_type):
        category_file = 'csv/Categories.csv'
        with open(category_file, "a") as file:
            file.write(f"{new_category}:{color} {category_type}\n")

    @staticmethod
    def get_all_categories():
        category_file = 'csv/Categories.csv'
        category_list = []
        with open(category_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "\n" in line:
                    line = line[:-1]
                    if len(line) == 0:
                        continue
                key = line.split(':')[0]
                value = line.split(':')[1][:-2].strip()
                category_type = line.split(':')[1][-1].strip()

                category_dict = {
                    'category_name': key,
                    'category_color': value,
                    'category_type': category_type
                }

                category_list.append(category_dict)

        return category_list

    @staticmethod
    def clear_category_file():
        category_file = 'csv/Categories.csv'
        with open(category_file, 'r+') as f:
            f.truncate(0)


class ExpenseCategories(Category):
    def __init__(self):
        super().__init__()
        self.category_dict = self.get_expense_category_dict()


class IncomeCategories(Category):
    def __init__(self):
        super().__init__()
        self.category_dict = self.get_income_category_dict()


# x = Category()
# expence = x.get_expence_category_dict()
# income = x.get_income_category_dict()
# print()
