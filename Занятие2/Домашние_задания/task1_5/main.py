import random
from string import ascii_lowercase, ascii_uppercase, digits

def pass_gen():
    sym = ascii_lowercase + ascii_uppercase + digits
    while True:
        yield "".join(random.sample(sym,8))


if __name__ == "__main__":
    a = pass_gen()
    for _ in range(10):
        print(next(a))
