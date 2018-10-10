import turtle as t


def draw_carpet(index, length):
    i = 0
    j = 0
    # sqaure is made
    for i in range(4):
        t.fd(length)
        t.right(90)
    # going up to make little sqaure now
    t.pu()
    t.left(90)
    t.fd(length / 2)
    t.right(90)
    t.backward(length / 2.5)
    t.pd()
    # making the three little sqaure on top
    for j in range(3):
        # making the little sqaure itself
        for i in range(4):
            t.fd(length / 6)
            t.right(90)
        t.pu()
        t.fd(length / 1.3)
        t.pd()
    t.pu()
    t.backward(length / 1.3)
    t.right(90)
    t.fd(length)
    t.pd()
    for j in range(2):
        # making the little sqaure itself
        for i in range(4):
            t.fd(length / 6)
            t.right(90)


def init():
    t.setup(900, 900)
    t.bgcolor("black")
    t.color("white")
    t.speed(100)
    t.pensize(2)


def main():
    length = 100
    index = 3
    init()
    draw_carpet(index, length)
    t.mainloop()


if __name__ == "__main__":
    main()
