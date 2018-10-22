# Author : Girish Kumar
import turtle as t


def recursive_rectangles_method1(depth, side):
    """
    This function draws the recursive rectangles
    :param depth: recursion depth
    :param side: length of the longest side
    :return: Sum of perimeters of all the rectangles
    """
    sum = 0
    # length and breadth of the rectangle
    length = side
    breadth = length / 1.618

    # a validation that's not required
    if depth <= 0:
        pass
    # base case
    elif depth == 1:
        # draw the base rectangle and return its perimeter
        for x in range(0, 2):
            t.forward(length)
            t.left(90)
            t.forward(breadth)
            t.left(90)
        sum = sum + 2 * (length + breadth)
        return sum
    else:
        # for a depth d in general
        """
        Explanation of the distance
        So, assume the length of the outermost rectangle is l
        Now, its breadth would be 1/1.618
        This will be the length of the inner rectangle. lets call it l2
        Now what will be the breadth of the inner rectangle? lets call it b2
        b2  = l2/1.618
            = (l/1.618)/1.618
        Now in order to draw the recursive rectangle you need to move l/2 + b2/2 distance and then draw the rectangle
        Refer the image for the math
        """
        # getting to the point where recursive rectangle needs to be called
        t.forward((length / 2) + (length / (1.616 * 1.618 * 2)))
        # the rectangle will be flipped. so turn 90
        t.left(90)
        # recursive call
        sum = sum + recursive_rectangles_method1(depth - 1, side / 1.618)
        # after recursion is done, turn 90 to get back to your original direction
        t.right(90)
        # move the remaining length and complete the first side(length) of the outermost rectangle
        t.forward(length - ((length / 2) + (length / (1.616 * 1.618 * 2))))
        # finish the rectangle
        t.left(90)
        t.forward(breadth)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(breadth)
        t.left(90)
        # sum the sides to the sum
        sum = sum + 2 * (length + breadth)
        return sum


def recursive_rectangles_method2(depth, side):
    """
    This function uses a different approach compared to the other one but the math involved in the distance
    is the same
    :param depth: Depth
    :param side: length of the longest side
    :return: total length of lines drawn
    """
    sum = 0
    length = side
    breadth = length / 1.618

    if depth == 0:
        return 0

    if depth > 0:
        t.up()
        t.forward((length / 2) + (breadth / (1.618 * 2)))
        t.left(90)
        t.down()
        sum = sum + recursive_rectangles_method2(depth - 1, side / 1.618)
        t.right(90)
        # pen up's so it would not draw when you traceback the origin/starting point
        t.up()
        # trace back to your origin
        t.backward((length / 2) + (breadth / (1.618 * 2)))
        t.down()
        # now draw the full outer rectangle
        for i in range(0, 2):
            t.forward(length)
            t.left(90)
            t.forward(breadth)
            t.left(90)
        sum = sum + 2 * (length + breadth)
        return sum


def main():
    side = int(input("Enter the length of the longest side : "))
    depth = int(input("Enter the depth of recursion : "))
    t.speed(5)
    # turtle_length = recursive_rectangles_method1(depth,side)
    turtle_length = recursive_rectangles_method2(depth, side)
    print("Total length of lines drawn : " + str(turtle_length))
    t.mainloop()


if __name__ == '__main__':
    main()
