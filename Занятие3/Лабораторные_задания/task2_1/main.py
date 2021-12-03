import json


def task() -> str:
        dict_numbers = {_: _ ** 2 for _ in range(1, 11)}  # TODO c помощью dict comprehension сформировать словарь
        return json.dumps(dict_numbers, indent=4)


if __name__ == "__main__":
    print(task())
