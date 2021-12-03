import json


def task():
    filename = "input.json"
    with open(filename, "r") as f:
        data = json.load(f)


    return max(data, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
