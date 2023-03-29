#   This file contains the various split methods
#   To be a valid method of splitting s into d components, it must follow these conditions:
#       s = a + b + ... + d
#       a > b > ... > d
#       a, b, ..., d > 0
#       a, b, ..., d are all positive integers
#   Then, for most of these methods...
#       a, b, ..., d are integer squares
#
#   By the way, 'n?' represents the sum from 1 to n.
#       In terms of Python, it is sum(range(1, n + 1))

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
def split_3(s, d, squares, min_squares):
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


#   Splits a sum, s, into 5 components
#       In other words, to enough components for a d = 5 array
def split_5(s, d, squares, min_squares):
    splits = []

    #   The upper bounds for each of these are whack
    #   The lower bounds are a guess (a very bad guess, evidently)
    for i in range(s - d, math.ceil(s / d), -1):

        if i not in squares:
            continue

        for j in range(s - 1, math.ceil((s - i) / (d - 1)) - 1, -1):

            if j not in squares:
                continue

            for k in range(s - 2, math.ceil((s - i - j) / (d - 2)) - 1, -1):

                if k not in squares:
                    continue

                for l in range(s - 3, math.ceil((s - i - j - k) / (d - 3)) - 1, -1):
                    m = s - i - j - k - l

                    if l not in squares or m not in squares:
                        continue

                    #   To get here, each of the d items must be a square
                    #       So, the count of squares is d
                    potential = [i, j, k, l, m, d]

                    #   Ensures a < b < ... < n
                    if i <= j or j <= k or k <= l or l <= m:
                        continue

                    #   Ensures each item is larger than zero > 0
                    if potential[-2] <= 0:
                        continue

                    splits.append(potential)

    return splits


#   A split function for the d = 5 case
#   This iterates only over values that are squares, skipping large swathes of bad values
#   There is the condition that 'min_squares = d'; each item is an integer square
def split_5_squares(s, d, squares, min_squares):
    #   This array will be filled with all valid splits of s into d components
    splits = []

    #   Converts the squares dictionary to an array
    #   This is so we can use indexing rather than keys
    sqa = [i for i in squares.keys() if i <= s]

    for i in range(4, len(sqa)):

        for j in range(3, len(sqa[:i])):

            #   If this condition is met, then all greater j's are bad values
            if sqa[i] + sqa[j] > s:
                break

            for k in range(2, len(sqa[:j])):

                #   If this condition is met, then all greater k's are bad values
                if sqa[i] + sqa[j] + sqa[k] > s:
                    break

                for l in range(1, len(sqa[:k])):

                    #   If this condition is met, then all greater l's are bad values
                    if sqa[i] + sqa[j] + sqa[k] + sqa[l] > s:
                        break

                    #   There are no degrees of freedom left for m
                    m = s - sqa[i] - sqa[j] - sqa[k] - sqa[l]

                    #   Check if m is a valid
                    if m >= sqa[l] or m not in squares:
                        continue

                    #   Creates the split
                    split = [sqa[i], sqa[j], sqa[k], sqa[l], m]

                    print(split, sum(split))

                    split.append(d)    # Appends the length to this tuple
                    splits.append(split)    #   Adds the split to the list of good splits

    #   Returns all valid splits
    return  splits


#   Recursively splits s into d components
#   NOTE: there is a hard limit due to Python recursion
#       s - d < 1000
#       For large numbers, an iterative approach is the only options
#       While the recursion limit can be changed, it's a pain in the butt
def split_recursive(s, d, squares, min_squares):
    #   Creates an array that will be populated with various ways to split s
    splits = []

    #   Does the recursive dance
    split_recursive_step(s, squares, d, splits, [], s - sum(range(d)))

    #   Returns all possible ways to split s in d components

    return splits


#   The approach of this function is to explore all splits by recursing in two directions:
#       One of the directions is iterating across i, a single component. This is iterating sideways.
#       The other direction is iterating down d, onto the next component. This is iterating downwards.
#   We always iterate to the next i, until it is too small for lower components
#       We bound i so we limit our search space.
#           It starts at 's - sum of higher order components'
#           It ends at 'd?', leaving room for lower order components
#   We only iterate down to the next component if i is an integer square.
#       This ensures that all splits are entirely integer squares.
#       When we iterate downwards, we set the starting i for the next level to be 'i - 1'.
#           This ensures a > b > ... > d
def split_recursive_step(s, squares, d, splits, split, i):

    #   Base case for downwards recursion
    if d == 0:
        if sum(split) == s: #   Checks that the sum is valid
            split.append(len(split))    #   Appends the length to this tuple
            splits.append(split)    #   Appends this tuple to the list of possible splits
        return

    #   Base case for sideways recursion
    #       There must be enough 'space' left for lower DoF items, hence the condition of 'd?'
    if i < sum(range(d + 1)):
        return

    #   Recurse sideways
    split_recursive_step(s, squares, d, splits, split.copy(), i - 1)

    #   Iterate downwards
    #       We only go downwards if the current item is an integer square
    if i in squares:
        #   If we got this far, then i is a good value
        split.append(i)

        #   Recurse downward
        split_recursive_step(s, squares, d - 1, splits, split.copy(), i - 1)
