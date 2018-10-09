import turtle as t


def draw_trunk():
    index = 5
    trunk_length = 100
    t.left(90)
    t.forward(trunk_length)
    draw_branches(trunk_length, index)


def draw_branches(length, index):
    if index == 0:
        print""
    else:
        t.left(45)
        t.fd(length / 2)

        # if index - 1 > 0:
        draw_branches(length / 2, index - 1)

        t.backward(length / 2)

        t.right(90)
        t.fd(length / 2)

        # if index - 1 > 0:
        draw_branches(length / 2, index - 1)

        t.backward(length / 2)
        t.left(45)
        return


def init():
    t.setup(600, 600)
    t.bgcolor("black")
    t.color("white")
    t.speed(4)
    t.right(90)
    t.forward(100)
    t.left(90)


def main():
    index = 2
    length = 100
    init()
    draw_trunk()
    t.mainloop()


if __name__ == "__main__":
    main()
