import turtle as t


def koch_snowflake(index, len):
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
