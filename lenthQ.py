def lenQ(n):
    if n > 0:
        return n + lenQ(n - 1)


def main():
    str = 3
    print lenQ(str)


if __name__ == "__main__":
    main()
