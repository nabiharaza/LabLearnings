import turtle as t


def triangle(itr, length):
    i = 0
    if itr <= 0:
        print
        return
    else:
        # first triangle on the left
        for i in range(3):
            t.fd(length)
            t.left(120)
        itr = itr - 1
        triangle(itr, length / 2)

        # second triangle on the right
        t.fd(length)
        for i in range(3):
            t.fd(length)
            t.left(120)
        # itr = itr - 1
        triangle(itr, length / 2)

        # going to the edge of the first
        t.left(120)
        t.fd(length)
        t.right(120)

        # top triangle
        for i in range(3):
            t.fd(length)
            t.left(120)
            # itr = itr - 1
        triangle(itr, length / 2)

        # going back to the start of the first triangle
        t.right(120)
        t.fd(length)
        t.left(120)

        itr = itr - 1
        triangle(itr, length / 2)
    return


def init():
    t.setup(1200, 1200)
    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(100)


def main():
    init()
    length = 100
    triangle(5, length)
    t.mainloop()


if __name__ == "__main__":
    main()
