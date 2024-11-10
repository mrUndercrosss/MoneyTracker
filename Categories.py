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

    def add_category(self, new_category, color, category_type):
        with open(self.category_file, "a") as file:
            file.write(f"{new_category}:{color} {category_type}\n")

    def __init__(self):
        self.color = None


class ExpenseCategories(Category):
    def __init__(self):
        super().__init__()
        self.category_dict = self.get_expence_category_dict()


class IncomeCategories(Category):
    def __init__(self):
        super().__init__()
        self.category_dict = self.get_income_category_dict()


# x = Category()
# expence = x.get_expence_category_dict()
# income = x.get_income_category_dict()
# print()
