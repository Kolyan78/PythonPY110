def pow_gen(base: int):
    step = 0
    while True:
        yield base ** step
        step += 1

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
