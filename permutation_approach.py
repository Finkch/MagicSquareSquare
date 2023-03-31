#   This is from an older version
#   Focuses on getting the permutations of splits to find a magic square

#   Heap's algorithm is used to efficiently find all permutations of a list
#       Swaps elements around until all permutations are obtained
def heaps(a, size, j, state):

    #   The return condition
    #       Appends the found permutation to the output array
    if size == 1:
        state[j].append(a.copy())

    for i in range(size):
        #   Recurse
        heaps(a, size - 1, j, state)

        #   Swaps elements based on whether the step is even or odd
        if size % 2 == 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

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