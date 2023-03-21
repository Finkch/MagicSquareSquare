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

import math

#   Checks if a split is valid. In other words, confirms these conditions:
#       a > b > c
#       a, b, c > 0
#       a + b + c = s
def is_valid_splits(s, splits):
    for row in splits:
        if row[0] <= row[1] or row[1] <= row[2]:
            return False
        if row[2] <= 0:
            return False
        if row[0] + row[1] + row[2] != s:
            return False
    return True

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


#   Counts the number of integer squares in an array
def count_squares(arr, squares):
    c_squares = 0

    for i in arr:
        if i in squares:    #   Checks the precomputed array of integer squares
            c_squares += 1

    return c_squares


#   Splits a sum, s, into d = 3 components
#       Returns an array of all such sums
#       As a note, s[i][0] > s[i][1] > s[i][2]
#           Order does not matter, so no need to repeat elements
def split_3(s, squares, min_squares):
    splits = [] #   Stores the ways to split up s
    bads = 0    #   Keeps track of how many 'continues' occurred

    #   Iterates such that i > j > k; i, j, k > 0; i + j + k = 0
    #       NOTE, the first item in range for j is bogus
    #           I couldn't think of a good range, so instead we're iterating
    #           over too many values and tossing the one's that don't work.
    #       i starts at s - 3, which (at max) allows j = 2 and k = 1
    #           3 is the SIGMA 1 to 'd - 1' (henceforth (d - 1)¡)
    #       i ends at ceil(s / 3), which guarantees the lower bound of i > j > k
    #           3 is the dimension of the array
    #       j starts at s - 1, which (as mentioned above) is bogus
    #       j ends at ceil((s - i) / 2), ensuring the lower bound
    #           2 is 'd - 1'
    #       k has no degrees of freedom, since it's s - i - j
    for i in range(s - 3, math.ceil(s / 3), -1):
        # for j in range(math.ceil((s - i) / 2) - 1, min(s - i - 1, i - 1), 1): #    Unused
        for j in range(s - 1, math.ceil((s - i) / 2) - 1, -1):

            #   Determines k, based on the current i & j
            k = s - i - j

            #   Gets the count of integer squares in the resulting tuple
            c = count_squares([i, j, k], squares)

            #   Tosses out bad values (as described above); ensures:
            #   i > j > k; i, j, k > 0
            #   Plus one final condition:
            #       The count of squares, c, is sufficiently large
            if i <= j or j <= k or k <= 0 or c < min_squares:
                bads += 1   #   For debugging purposes, counts values tossed out (wasted iterations)
                continue    #   Tosses this tuple out

            #   Appends the tuple to the list of ways to split n
            splits.append([i, j, k, c])

    #   Prints the amount of 'bad' tuples created
    print(bads)

    #   Returns all the ways to split s into 3 components
    return splits


#   Gets the ball rolling
def main():
    #   The maximum number to search up to
    maximum = 100

    #   The current sum to split up and check if it is a magic square
    s = maximum

    #   The minimum number of integer squares required per tuple
    min_squares = 2

    #   An array to quickly lookup square roots
    squares = create_squares(maximum)

    #   With s = 100...
    #       Without integer squares, len(splits) = 784
    #       With integer squares 1, len(splits) = 264 (roughly 's / log_10(s)')
    #       With integer squares 2, len(splits) = 30
    #       With integer squares 3, len(splits) = 0

    #   Splits s into 3 components
    splits = split_3(s, squares, min_squares)

    print(squares)

    print("\n\n")

    for i in splits:
        print(i)

    print("\nIs valid:", is_valid_splits(s, splits), "\nLength:", len(splits))



main()