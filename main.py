import math

#   Fills the array, arr, with all squares smaller than max
#   Used for a quick lookup rather than doing lots of square roots
#       If i is a square, then the item at the index i is the square of i
#       Must use a try-catch to check, in case the item at index i is not a square
def squares_array(arr, maximum):
    i = 0
    while i ** 2 < maximum:
        arr[i ** 2] = i
        i += 1


#   Used for debugging
#   Prints the current step, including the potential magic array and the array of its sums
#       Will only print if the global variable should_print is True
def print_step(arr, sums, iter):
    if not should_print:
        return

    #   Prints the potential magic array
    print(iter, ": ", arr, sep="", end="\t")

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

#   Heap's algorithm is used to efficiently find all permutations of a list
#       Swaps elements around until all permutations are obtained
def heaps(a, size, j, state):

    #   The return condition
    #       Appends the found permutation to the output array
    if size == 1:
        state[j].append(a.copy())

    for i in range(size):
        #   Recurses
        heaps(a, size - 1, j, state)

        #   Swaps elements based on whether the step is even or odd
        if size % 2 == 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


#   Checks if all elements in an array are the same
#       Used to check if all sums in a potential magic array are equal
def all_equal(to_check):
    for i in to_check[1:]:
        if i != to_check[0]:
            return False
    return True


#   For a number s, splits it into m^2 components
#   For the 3x3 magic square squared,
#       At least 7, 8, or 9 must be squares of integers
#       All must be distinct
def split(splits, s, m):


    return

def split_3(splits, s, squares):

    for i in range(s - 3, int(s / 3) + 1, -1):
        for j in range(s - i - 1, 2, -1):
            k = s - i - j
            to_check = [i, j, k]

            count_of_squares = check_split(to_check, squares)

            if count_of_squares < 2 or i <= j or j <= k:
                continue
            else:
                to_check.append(count_of_squares)

            splits.append(to_check)


def check_split(to_check, squares):
    return count_squares(to_check, squares)


def count_squares(to_check, squares):
    sqrs = 0
    for i in to_check:
        try:
            if squares[i] != 0:
                sqrs += 1
        except:
            pass

    return sqrs




#   This code DOES NOT WORK
#   I'm leaving it here because I want to come back to it
#       It feels like, if I can get it to work, it would be a particularly elegant solution
#   Given the array of possibles, gives all unique permutations
#       Does so through a recursive method
def get_permutations_recursive(check, possibles, i, j):

    if len(possibles) == 0:
        check[i][j] = possibles[0][i]
        return

    if len(possibles[0]) == 0:
        get_permutations_recursive(check, possibles[1:], 0, j + 1)

    print(i, j, "\t\tDims: ", len(possibles), len(possibles[0]), "\t\t", possibles[0][i])

    get_permutations_recursive(check, [*check[:i], check[i][1:], *check[i+1:]] , i + 1, j)

#   Gets the permutations of tuples through iteration over n!^n items,
#   which is effectively iterating over n for loops of length n! each,
#   and using an equation using a modulus to construct the unique permutation
def get_permutations_mod(check, possibles):
    #   Gets the dimensions of each array
    n = len(possibles)
    n_fact = len(possibles[0])
    all_permutations = n_fact ** n

    #   Iterates over all permutations of the n tuples
    for i in range(all_permutations):

        #   Creates a new array to check
        check.append([])

        #   Fills the new array with one of the necessary tuples
        #   to create a unique entry
        for j in range(len(possibles)):
            #   Determines which tuples to grab
            mod = int(i / (n_fact ** (n - j - 1))) % n_fact
            check[-1].append(possibles[j][mod]) #   Appends the tuples to the appropriate potential


#   Iterates over all combinations of a 3x3 array
#       Does so though a harc-coded 3 deep for loop
def get_permutations_3(check, possibles):
    #   Gets n!
    #       Which is the length of each tuple in the possibles array
    permutations = len(possibles[0])

    #   Iterates over all combinations
    for i in range(permutations):
        for j in range(permutations):
            for k in range(permutations):
                #   Obtains a unique permutation of each tuple
                check.append([possibles[0][i], possibles[1][j], possibles[2][k]])


#   Iterates over all combinations of a 4x4 array
#       Does so though a harc-coded 4 deep for loop
def get_permutations_4(check, possibles):
    #   Gets n!, the length of each tuple in the possibles array
    permutations = len(possibles[0])

    #   Iterates over all combinations
    for i in range(permutations):
        for j in range(permutations):
            for k in range(permutations):
                for l in range(permutations):
                    #   Obtains a unique permutation of each tuple
                    check.append([possibles[0][i], possibles[1][j], possibles[2][k], possibles[3][l]])


#   Given the results of split, tries to place the items into a magic square squared
#       On a 3x3 matrix...
#           Component 4 must be used four times
#           Components 0, 2, 6, 8 must all be used three times
#           Components 1, 3, 5, 7 must all be used three times
#   There are technically 9! ways of arranging the items, aka 362 880 ways
#       However, based on the previous restriction of A_i + B_i + C_i = N, the search space is (3!)^3
#       Then due to the symmetry around only the first i (the choice of first is arbitrary), it's ((3!)^3)/2
#       In short, the search space is 108 items
#           That is if we only swap items around within one i
def magic(magic_arr):

    #   The dimension of the matrix
    n = len(magic_arr)

    #   Calculates the number of ways to arrange one tuple
    permutations = math.factorial(n)

    #   Given the potential magic array, produce all permutations of the elements within each tuple
    #       The order of the tuples are not swapped.
    #       Only the order of elements within a tuple are swapped.
    possibles = []
    for i in range(n):
        possibles.append([])
        heaps(magic_arr[i], n, i, possibles)

    #   Print out all permutations
    if should_print:
        print("All permutations of each item within every tuple:")
        for l in possibles:
            print(l)
        print()


    #   Creates the potential magic arrays
    check_arr = []
    get_permutations_mod(check_arr, possibles)

    index = 0   #   The index of the iteration, for printing purposes
    for i in check_arr:
        #   Produces an array of all the sums of the potential magic square
        to_check = sum_magic(i)

        #   Debug print-out
        print_step(i, to_check, index)
        index += 1

        #   Checks if all the sums are equal
        #       If so, it is a valid magic square, and it is returned
        if all_equal(to_check):
            return i

    return


#   Puts split and magic together
def magic_dance(n):
    return


#   Describes some meta-variables and initiates the rest
def main():
    # maximum = 1e9 # A reasonable max, just shy of half as big as sys.maxsize
    maximum = 121

    #   Creates a very big array
    squares = {}

    #   Describes the dimensions of the magic square
    dim = 3

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

    #   Prints out the valid magic square, if is exists
    if the_magic_arr:
        S = 0
        for l in the_magic_arr[0]:
            S += l

        print("\nThe magic array (S = ", S, "):", sep="")
        for l in the_magic_arr:
            print(l)
    else:
        print("No magic array found...")
    print("\nAll done!")


    splits = []
    split_3(splits, 100, squares)


    for i in splits:
        print(i)

    print(len(splits))

    print("\n\n", squares)



should_print = True

main()
