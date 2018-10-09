import turtle as t


def polyFlow(angle, index):
    print index
    length = 100
    t.left(angle)
    i = 0
    if index == 0:
        print " "

        return
    else:
        for i in range(5):
            t.forward(length)
            t.right(180 - 108)
        index = index - 1
        # print index
    polyFlow(36, index)
    return


def init():
    t.setup(1200, 800)
    t.bgcolor("black")
    t.pensize(2)
    t.color("white")
    t.speed(9)


def main():
    init()
    polyFlow(45, 10)
    t.mainloop()


if __name__ == "__main__":
    main()
