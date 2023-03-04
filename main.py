import math


#   Fills the array, arr, with all squares smaller than max
#   Used for a quick lookup rather than doing lots of square roots
#       If the i-th entry is a square, it contains its square root (e.x.: arr[9] contains 3)
#       Otherwise it contains 0
def squares_array(arr, maximum):
    i = 0
    while i ** 2 < maximum:
        arr[i ** 2] = i
        i += 1

#   Used for debugging
#   Prints the current step, including the potential magic array and the array of its sums
#       Will only print if the global variable should_print is True
def print_step(arr, sums):
    if not should_print:
        return

    #   Prints the potential magic array
    print(arr, end="\t")

    #   Prints the sums of the potential magic array
    print(sums)


#   Performs a sum over the magic array
def sum_magic(magic_arr):
    #   Gets the dimensions of the matrix
    #       It is guaranteed to be an nxn matrix
    n = len(magic_arr)

    # The total ways to sum a magic square
    #   There are n contributions from the tuples
    #   An additional n contributions from the columns
    #   And two final contributions from the diagonals
    sums = [0] * (2 * n + 2)

    #   Row sums
    for i in range(n):
        for j in range(n):
            sums[i] += magic_arr[j][i]

    #   Vertical sums
    for i in range(n):
        for j in range(n):
            sums[n + i] += magic_arr[i][j]

    #   First diagonal
    for i in range(n):
        sums[-2] += magic_arr[i][i]

    #   Second diagonal
    for i in range(n):
        sums[-1] += magic_arr[n - i - 1][i]

    return sums


#   NEEDS TO BE UPDATED
#   Given a 3x1 matrix (or a tuple of width 3), produces a permutation based upon an index
#   Current implementation does so the lazy way
#       The index is used as a lookup for the pre-computed permutations
def produce_tuple(arr, i, case):
    if case == 0:
        return [arr[i][0], arr[i][1], arr[i][2]]
    elif case == 1:
        return [arr[i][0], arr[i][2], arr[i][1]]
    elif case == 2:
        return [arr[i][2], arr[i][0], arr[i][1]]
    elif case == 3:
        return [arr[i][2], arr[i][1], arr[i][0]]
    elif case == 4:
        return [arr[i][1], arr[i][0], arr[i][2]]
    elif case == 5:
        return [arr[i][1], arr[i][2], arr[i][0]]


#   Checks if all elements in an array are the same
#       Used to check if all sums in a potential magic array are equal
def all_equal(to_check):
    for i in to_check[1:]:
        if i != to_check[0]:
            return False
    return True


#   For a number n, splits it into 9 components
#       At least 7, 8, or 9 must be squares of integers
#       All must be distinct
#   The largest size of any component is reasonably n / 3
#       For completeness's sake, we'll consider up to n / 2
def split(n):
    return


#   Given the results of split, tries to place the items into a magic square squared
#       Component 4 must be used four times
#       Components 0, 2, 6, 8 must all be used three times
#       Components 1, 3, 5, 7 must all be used three times
#   There are technically 9! ways of arranging the items, aka 362 880 ways
#       However, based on the previous restriction of A_i + B_i + C_i = N, the search space is (3!)^3
#       Then due to the symmetry around only the first i (the choice of first is arbitrary), it's ((3!)^3)/2
#       In short, the search space is 108 items
#           That is if we only swap items around within one i
def magic(magic_arr):

    #   Calculates the number of ways to arrange one tuple
    permutations = math.factorial(len(magic_arr))

    #   Iterates over all permutations of the potential magic array
    for i in range(permutations):
        for j in range(permutations):
            for k in range(permutations):

                #   Given the potential magic array, produce a single permutations of the elements within each tuple
                #       The order of the tuples are not swapped.
                #       Only the order of elements within a tuple are swapped.
                check_arr = [produce_tuple(magic_arr, 0, i),
                             produce_tuple(magic_arr, 1, j),
                             produce_tuple(magic_arr, 2, k)]

                #   Produces an array of all the sums of the potential magic square
                to_check = sum_magic(check_arr)

                #   Debug print-out
                print_step(check_arr, to_check)

                #   Checks if all the sums are equal
                #       If so, it is a valid magic square, and it is returned
                if all_equal(to_check):
                    return check_arr

    return


#   Puts split and magic together
def magic_dance(n):
    return


#   Describes some meta-variables and initiates the rest
def main():
    # maximum = 1e9 # A reasonable max, just shy of half as big as sys.maxsize
    maximum = 121

    #   Creates a very big array
    squares = [0] * int(maximum)

    #   Fills the very big array with lots and lots of square roots in appropriate places
    #   If the i-th entry is a square, it contains its square root (e.x.: arr[9] contains 3, arr[3] contains 0)
    squares_array(squares, maximum)

    # for i in range(maximum):
    #    magic_dance(i)

    magic_arr = [[4, 9, 2],
                 [3, 5, 7],
                 [8, 1, 6]]

    false_arr = [[2, 4, 9],
                 [3, 5, 7],
                 [1, 6, 8]]

    the_magic_arr = magic(false_arr)

    #   Prints out the valid magic square
    for l in the_magic_arr:
        print(l)

    print("All done!")


should_print = True

main()