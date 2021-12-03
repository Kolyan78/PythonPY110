def geo_prog(b, q):
    yield b
    n = 1
    while True:
        yield b * pow(q, n)
        n += 1

if __name__ == "__main__":
    a = geo_prog(2, 6)
    for _ in range(10):
        print(next(a))
