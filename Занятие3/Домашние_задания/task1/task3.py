# Написать генератор, возвращающий по одному слову текстового файла,
# при этом не загружая в память весь файл.
# В качестве разделителя слов использовать символ пробела.
# практика 1-1 используя итератор сделать генератор

def get_word(f):
    while True:
        word = ""
        while True:
            letter = f.read(1)
            if letter == " ":
                break
            else:
                word += letter
        yield word


with open("textfile.txt", "r", encoding='utf8') as f:
    for _ in range(5):
        print(next(get_word(f)))