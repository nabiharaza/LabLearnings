import turtle as t


def draw_snowflake(index, length):
    if index == 0:
        return
    else:
        for i in range(6):
            t.left(60)
            t.forward(length)
            draw_snowflake(index - 1, length / 3)
            t.backward(length)
        return


def init():
    t.setup(900, 900)
    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(600)


def main():
    init()
    # t.Screen.tracer(0)
    draw_snowflake(4, 100)
    t.mainloop()


if __name__ == "__main__":
    main()

    # # if index > 1:
    # #      for i in range(6):
    # #         t.left(60)
    # #         t.fd(length)
    # #         # draw_snowflake(index-1, length / 2)
    # #         # index = index - 1
    # #         # t.bk(100)
    #         draw_snowflake(index-1, length / 2)
