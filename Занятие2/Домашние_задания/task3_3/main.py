def decorator(fn):
    def wrapper(*args, **kwargs):
        def is_iter(i):
            try:
                (_ for _ in i)
            except:
                return False
            else:
                return True

        for i in args:
            if not(is_iter(i)):
                raise TypeError(f"Объект '{i}' не является итерируемым")
        for i, j in kwargs.items():
            if not(is_iter(j)):
                raise TypeError(f"Объект '{i}={j}' не является итерируемым")
        fn()
    return wrapper


if __name__ == "__main__":
    @decorator
    def func():
        print("Начало функции")
        pass
        print("Конце функции")

    func([1, 4, 3], 3, "str", [1, 2, 3], x=5, y=[3, 6, 9])

