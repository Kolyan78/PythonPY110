# Задание 4.
# Напишите скрипт для сложения двух заданных списков, используя map и lambda.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 0]
print(list(map(lambda x, y: x + y, list1, list2)))