import turtle as t


def tree(index, length):
    # t.left(90)
    # t.fd(length)
    # t.left(90)

    if index == 0:
        return
    else:
        # for i in range(3):
        t.left(45)
        t.fd(length)
        tree(index - 1, length / 2)

        t.backward(length)
        t.right(45)
        t.fd(length)
        tree(index - 1, length / 2)

        t.backward(length)
        t.right(45)
        t.fd(length)
        tree(index - 1, length / 2)

        t.backward(length)
        t.left(45)

        # tree(index-1, length/2 )
        # t.backward(length)
        return


def init():
    t.setup(1200, 1200)

    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(1)
    t.left(90)


def main():
    init()
    length = 100
    tree(3, length)
    t.mainloop()


if __name__ == "__main__":
    main()
