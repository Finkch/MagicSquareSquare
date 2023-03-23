#   This file contains the various split methods

import math


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
    #bads = 0    #   Keeps track of how many 'continues' occurred

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
                #bads += 1   #   For debugging purposes, counts values tossed out (wasted iterations)
                continue    #   Tosses this tuple out

            #   Appends the tuple to the list of ways to split n
            splits.append([i, j, k, c])

    #   Prints the amount of 'bad' tuples created
    #print(bads)

    #   Returns all the ways to split s into 3 components
    return splits
