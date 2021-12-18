def get_list(f):
    list_ = ""
    for _ in f:
        list_ += _
    return list_
    #return [_ for _ in f]


if __name__ == "__main__":
    FIRST = "1.txt"
    SECOND = "2.txt"
    with open(FIRST, "r") as f1, open(SECOND, "r") as f2:
        print(get_list(f1))
        print(get_list(f2))
