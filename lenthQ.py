def lenQ(n):
    if n > 0:
        return n + lenQ(n - 1)


def main():
    y = 0
    for i in range(10, 1):
        print i


if __name__ == "__main__":
    main()
