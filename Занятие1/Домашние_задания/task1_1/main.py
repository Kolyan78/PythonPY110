def enumerate_ (iterable, start=0):
    return zip(range(start, start + len(iterable)), iterable)

if __name__ == "__main__":
    seq = list('абвгде')
    for i, val in enumerate_(seq, start=1):
        print(f'№ {i} => {val}')