def decorator(fn):
    def wrapper(*args):
        for i in args:
            if isinstance(i, int):
                print(f"Аргумент '{i}' является целочисленным")
            else:
                print(f"Аргумент '{i}' не является целочисленным")
        fn()
    return wrapper


if __name__ == "__main__":
    @decorator
    def func(*args):
        print("Выполняется сама функция")
        pass
        print("Функция выполнилась")

    func(1, 2, "str", 45, [1, 2, 3], 0.5)

