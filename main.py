import math

#   Fills the array, arr, with all squares smaller than max
#   Used for a quick lookup rather than doing lots of square roots
#       If the i-th entry is a square, it contains its square root (e.x.: arr[9] contains 3)
#       Otherwise it contains 0
def squares_array(arr, maximum):
    i = 0
    while i**2 < maximum:
        arr[i**2] = i
        i += 1

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
#   There are 9! ways of arranging the items, aka 362 880 ways
def magic(magic_arr):
    return

#   Puts split and magic together
def magic_dance(n):
    return

#   Describes some meta-variables and initiates the rest
def main():
    maximum = 1e9 # A reasonable max, just shy of half as big as sys.maxsize

    #   Creates a very big array
    squares = [0] * int(maximum)

    #   Fills the very big array with lots and lots of square roots in appropriate places
    #   If the i-th entry is a square, it contains its square root (e.x.: arr[9] contains 3, arr[3] contains 0)
    squares_array(squares, maximum)

    for i in range(maximum):
        magic_dance(i)



main()