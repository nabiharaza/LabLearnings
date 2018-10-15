import turtle as t


def triangle(index, lenght):
    if index == 0:
        return
    else:
        # making the first traingle
        for i in range(3):
            t.fd(lenght)
            t.left(120)
        triangle(index, lenght / 2)
        t.fd(lenght)
        #making the second triangle
        for i in range(3):
            t.fd(lenght)

            t.left(120)
        triangle(index, lenght / 2)
        # going back from the second trinagle
        t.right(180)
        t.fd(lenght)
        #going up now
        t.right(120)
        t.fd(lenght)
        t.left(60)

        #now finally making the third triangle
        for i in range(3):
            t.left(120)

            t.fd(lenght)
        triangle(index, lenght / 2)
        # getting back to the start
        t.left(60)
        t.fd(lenght)
        t.left(60)
        t.fd(lenght)
        t.right(60)
        t.right(180)
        triangle(index - 1, lenght /2)

    return



def init():

    t.setup(1200, 1200)
    t.bgcolor("black")
    t.color("white")
    t.pensize(2)
    t.speed(120)


def main():
    init()
    length = 150
    triangle(3, length)
    t.mainloop()


if __name__ == "__main__":
    main()

# def triangle(itr, length):
#     i = 0
#     if itr <= 0:
#         print
#         return
#     else:
#         # first triangle on the left
#         for i in range(3):
#             t.fd(length)
#             t.left(120)
#         itr = itr - 1
#         triangle(itr, length / 2)
#
#         # second triangle on the right
#         t.fd(length)
#         for i in range(3):
#             t.fd(length)
#             t.left(120)
#         # itr = itr - 1
#         triangle(itr, length / 2)
#
#         # going to the edge of the first
#         t.left(120)
#         t.fd(length)
#         t.right(120)
#
#         # top triangle
#         for i in range(3):
#             t.fd(length)
#             t.left(120)
#             # itr = itr - 1
#         triangle(itr, length / 2)
#
#         # going back to the start of the first triangle
#         t.right(120)
#         t.fd(length)
#         t.left(120)
#
#         itr = itr - 1
#         triangle(itr, length / 2)
#     return
