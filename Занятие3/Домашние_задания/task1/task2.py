# Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.
# f.read(3) ... yield
def get3(f):
    while True:
        yield f.read(3)


with open("textfile.txt", "r", encoding='utf8') as f:
    for _ in range(10):
        print(next(get3(f)))
