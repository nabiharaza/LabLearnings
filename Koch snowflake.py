import turtle as t


def koch_snowflake(index, len):
    if index == 0:
        return
    else:
        for i in range(1):
            t.right(60)
            t.forward(len / 4)
            t.right(60)
        for j in range(3):
            for i in range(3):
                t.right(60)
                t.forward(len / 6)
                t.left(120)
                t.forward(len / 6)
            t.right(60)
            t.fd(len / 6)
            t.right(60)
            t.fd(len / 6)
            # t.left(60)
        t.right(60)
        t.fd(len / 6)
        t.left(120)
        t.fd(len / 6)
        t.right(60)
        t.fd(len / 6)
        # t.forward(len)
        koch_snowflake(index - 1, len)
        return


def init():
    t.setup(1200, 1200)

    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(10)
    # t.pu()
    # t.left(60)
    # t.fd(50)
    # t.pd()


def main():
    init()
    length = 100
    koch_snowflake(6, length)
    t.mainloop()


if __name__ == "__main__":
    main()

# if index == 0:
#       return
#   else:
#       t.right(60)
#       # for i in range(2):
#       t.fd(len)
#       t.left(120)
#
#       t.fd(len)
#
#       koch_snowflake(index-1, len)
