expense_categories = [
    {'Еда': []},
    {'Транспорт': []},
    {'Развлечения': []},
    {'Компы': []},
    {'Прочее': []},
    {'Test': []}
]

x = expense_categories[0].get('Еда').append(20)
y = expense_categories[0].get('Еда').append(40)
for categ in expense_categories:
    key = list(categ.keys())[0]
    print(key)
