def pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * pow(x, n - 1)


if __name__ == '__main__':
    print(pow(2, 4))
