import turtle as t


def triangle(index, len):
    for i in range(3):
        t.fd(len)
        t.right(120)
    t.fd(len / 2)


def init():
    t.setup(1200, 1200)

    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(10)


def main():
    init()
    length = 100
    triangle(2, length)
    t.mainloop()


if __name__ == "__main__":
    main()
