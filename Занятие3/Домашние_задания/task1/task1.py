# Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения. Результаты должны накапливаться в файле.
from random import randint
def my_decorator(func):
    def wrapper(x, y):
        with open("output.txt", "a") as f:
            f.write(func(x, y))
    return wrapper

@my_decorator
def pow_(x, y):
    return(f"{x}^{y} = {pow(x, y)}\n")


print(pow_(randint(0,10), randint(0,10)))