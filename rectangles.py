# @author nabiharaza

import turtle as t


def rectangles(index, len, total):
    slen = len / 1.618
    if index == 0:
        return
    else:
        # making the rectangle
        for i in range(4):
            t.fd(len)
            total = len + total
            t.left(90)

            t.fd(slen)
            total = slen + total
            t.left(90)
        # now making for level 2

        t.fd(len / 3)
        total = len / 3 + total
        t.left(90)
        t.fd(slen)
        total = slen + total

        # went up for first split
        t.right(90)
        t.fd(len / 3)
        total = len / 3 + total
        t.right(90)
        t.fd(slen)

        # made the second split
        # going in the half

        t.backward(slen)
        total = slen + total
        t.right(90)
        t.fd(len / 3)
        total = len / 3 + total
        t.left(90)
        t.fd(slen / 2)
        total = slen + total
        t.left(90)

        # now making the turtle go exactly where it starts
        # starting the recursion
        rectangles(index - 1, len / 3, total)

    return total


def init():
    t.setup(900, 900)
    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(3)


def main():
    init()
    index = 2
    length = 100
    total = 0
    tlen = rectangles(index, length, total)
    print "Your Total Length is : %d" % tlen
    t.mainloop()


if __name__ == "__main__":
    main()
