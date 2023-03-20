#   Try 2
#   This algorithm is founded on an observation:
#       If s can create a valid magic array, then splits (an array
#       containing all ways to split s into d elements) itself
#       must contain all 2 * d + 2 sums with d distinct elements.
#       There's no need to choose d tuples then permute the elements
#       within the arrays until a magic array is found.
#   This is the approach:
#       Create an array, splits, that contains all ways to split s into d elements.
#       Searches through splits for 2 * d + 2 tuples that obey these properties (d = 3 case):
#           Four items appear exactly two times in the 8 tuples;
#           Four items appear exactly two three in the 8 tuples; and,
#           One item appears exactly four times in the 8 tuples.
#       In addition:
#           At just about each step, there are checks to discard invalid items.
#           At just about each step, there are constraints to trim the search space.
#           At the beginning, an array is creating to allow quick searches whether an item is a integer square.

#   Creates a dictionary from 1 to maximum
#       The keys are an integer square
#       The values are the integer square root of the key
def create_squares(maximum):
    squares = {}

    #   The keys range from 1 to maximum^2
    #   The values range from 1 to maximum
    for i in range(1, int(maximum ** (1/2) + 1)):
        squares[i ** 2] = i
    return  squares


#   Gets the ball rolling
def main():
    #   The maximum number to search up to
    maximum = 100

    #   An array to quickly lookup square roots
    squares = create_squares(maximum)

    print(squares)


main()