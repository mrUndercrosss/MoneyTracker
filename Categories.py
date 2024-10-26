class Category:

    category_file = 'csv/Categories.csv'

    def get_category_list(self):
        category_list = []
        with open(self.category_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                category_list.append(line.strip())

        return category_list

    def add_category(self, new_category):
        with open(self.category_file, "a") as file:
            file.write(f"{new_category}\n")

    def __init__(self):
        self.category_list = self.get_category_list()
