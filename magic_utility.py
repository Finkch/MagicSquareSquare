#   Various helpful methods


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

#   Checks if the array can construct a magic square with at least 7 integer squares
def has_enough_squares(splits):
    #   Creates an array that tracks the occurrences of the counts of squares within each tuples
    counts = [0] * 4

    #   Checks the count of integer squares in each tuple
    for i in splits:
        counts[i[-1]] += 1

    #   Returns the counts
    return counts


def sort_on_first(element):
    return element[0]

#   Counts the occurrences of each value in each tuple
#       This is to throw out candidates and tuples that won't contribute
#   Oh my god, on a test value of 62, this removes a whopping 4 tuples out of 121.
#   3% for _this_ much work!
#       AAAAAAAHHH
def count_occurrences(splits, s, threshold):

    #   Creates an array of tuples
    #       Each tuple has two elements:
    #           The first is the count of occurrences
    #           The second is the index (so index is preserved through sorting on occurrences)
    occ = [[0, i] for i in range(0, s - 1)]

    #   Counts the occurrences of a number in splits
    for i in splits:
        for j in i[:-1]:
            occ[j][0] += 1

    #   Removes items that only occur once (aren't candidates for a magic array)
    occ = [i for i in occ if i[0] >= threshold]

    #   Sort them
    #       For good measure, I suppose
    occ.sort(key=sort_on_first, reverse=True)

    #   Creates a dictionary for quicker lookups
    occ_out = {}
    for i in occ:
        occ_out[i[1]] = i[0]

    #   Removes ineligible tuples from splits
    #t = [i for i in splits if (j for j in i) if j not in occ_out]
    #t = [i for i in splits if (j for j in i) not in occ_out.keys()]
    t = []  #   If it ain't broke, don't fix it...
    for i in splits:
        good = True
        for j in i:
            if j not in occ_out.keys():
                good = False
                continue
        if good:
            t.append(i)

    #   Returns
    return t

