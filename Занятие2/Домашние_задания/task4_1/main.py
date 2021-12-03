def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    line = pairwise(pts)
    c = 0
    for _ in range(len(pts)-1):
        x = next(line)
        gen = (i for i in x)
        res = list(map(lambda i,j: i-j, next(gen), next(gen)))
        c += pow(pow(res[0], 2) + pow(res[1], 2), 0.5)
    print(f"Длина линии равна: {round(c, 3)}")