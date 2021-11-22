# Задание 3.
# Напишите скрипт для преобразования заданного списка кортежей в список строк с помощью функции map().
#
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']
#
# Original list of tuples:
# [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
# Convert the said list of tuples to a list of strings:
# ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']

def conv(x):
    return " " . join(x)


list_ = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
list2 = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

print(list(map(conv, list_)))
print(list(map(conv, list2)))
