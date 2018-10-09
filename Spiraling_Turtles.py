import turtle as t


# testing the basic program with spirals
# spiral(200,90,0.9,10)
# spiral(200,72,0.97,10)
# spiral(200,80,0.95,10)
# spiral(200,121,0.95,15)
# spiral(200,95,0.93,10)

def spiral(sideLen, angle, scaleFactor, minLength):
    """
    this draws spiral figure recursively
    :pre: pos(0,0) relative, pendown, heading east
    :post: end of pattern relative, pendown, heading in the direction of last line drawn
    :param sideLen:
    :param angle:
    :param scaleFactor:
    :param minLength:
    :return:
    """
    if minLength >= 200:
        print
        return
    else:
        for i in range(5):
            t.left(angle)
            minLength = minLength * 1.1
            t.forward(minLength)

        print sideLen
        spiral(200, 95, 1.9, minLength)
        return


def init():
    t.setup(900, 900)
    t.bgcolor("black")
    t.color("white")


def main():
    init()
    spiral(200, 95, 1.2, 10)
    t.mainloop()


if __name__ == "__main__":
    main()
