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
def has_enough_squares(splits, d):
    #   Creates an array that tracks the occurrences of the counts of squares within each tuples
    counts = [0] * (d + 1)


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
#       This 4 remains constants as s grows!
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


#   Removes items from split which have an insufficient amount of root sums
#   to form an integer root magic square (thus cannot be bi-magic)
#       The structure of splits is...
#          [..., [[A_i, B_i, ..., D_i, sq_i], [a_i, b_i, ..., d_i, s_i]], ...]
#       ...so the root sums are located in splits[i][1][d] or more simply splits[i][-1][-1]
def count_root_sums(splits, s, d):

    #   Creates a dictionary counting the occurrences of each item
    occ = {}

    #   Fills the dictionary by counting items
    for i in splits:
        z = i[-1][-1]
        if z not in occ.keys():
            occ[z] = 0
        occ[z] += 1


    #   Removes items that only occur once (aren't candidates for a magic array)
    #       To be a candidate, the sum must appear once per row, once per column, and once per diagonal
    #           Which is 2 * d + 2 times
    occ = {i:occ[i] for i in occ.keys() if occ[i] >= (2 * d + 2)}
    #occ = {i:occ[i] for i in occ.keys() if occ[i] >= 5} #   For testing

    #   Removes the tuples without sufficient occurrences of the root sums
    #       I.e. it removes items whose root sum is not a key in occ
    splits = [i for i in splits if i[-1][-1] in occ.keys()]

    return splits

#   This function returns an array where each tuple contains pairs of items
#   whose root sum is the same.
def decouple_over_root_sum(splits, s):
    out = []    #   The output array
    keys = {}   #   The key is the root sum, the value is the index of that root sum
    index = 0

    for i in splits:
        root_sum = i[-1][-1]    #   Grabs the root sum

        #   Adds the root sum and its index if it is new
        if root_sum not in keys:
            keys[root_sum] = index
            out.append([])  #   Adds an array into which matching root sums can be placed
            index += 1

        #   Adds this root sum's tuples to the output array
        out[keys[root_sum]].append(i)

    #   Prefaces each tuple with the magic constant, root sum, and the count of root ums
    for i in out:
        i.insert(0, [s, i[0][-1][-1], len(i)])

    return out


#   Returns a dictionary that maps a number that appears in splits to
#   all tuples in which that number makes an appearance.
#   For the case when the first tuple describes the rest's shape.
def create_occurrences_dictionary_shaped(splits):

    #   The keys are a set of numbers appearing within the splits
    #   The values are all tuples in which the key appears
    occs = {}

    for i in splits[1:]:        #   Ignores the first item (describes the shape of splits)
        for j in i[:-1]:         #   Ignores the last item (describes the count of squares OR root sum)
            if j not in occs:   #   If the key does not exist, create an empty tuple
                occs[j] = []
            occs[j].append(i)   #   Appends that tuple to the appropriate dictionary entry

    #   Returns the occurrence dictionary
    return  occs

#   The same as the above, except when the meta-data elements
#   describing the shape and contents are removed.
def create_occurrences_dictionary_unshaped(splits):

    #   The keys are a set of numbers appearing within the splits
    #   The values are all tuples in which the key appears
    occs = {}

    for i in splits:        #   Ignores the first item (describes the shape of splits)
        for j in i:         #   Ignores the last item (describes the count of squares OR root sum)
            if j not in occs:   #   If the key does not exist, create an empty tuple
                occs[j] = []
            occs[j].append(i)   #   Appends that tuple to the appropriate dictionary entry

    #   Returns the occurrence dictionary
    return  occs

#   Checks if two arrays are mutually unique.
#       In other words, they share no values.
def is_unique_tuple(arr1, arr2):
    seen = set(arr1)
    return not any(i for i in arr2 if i in seen)

#   Checks whether an array exclusively contains non-unique values.
#       In other words, it shares all values with the set.
def only_contains_non_unique(base_set, to_check):
    return not any(i for i in to_check if i not in base_set)

#   Checks whether the arrays are the same
def equivalent_tuple(arr1, arr2):
    return all(arr1[i] == arr2[i] for i in arr1)

#   Creates a hash-map of each split
def create_occurrence_set(splits):
    return set(str(i) for i in splits)

#   Checks if a given split is in the hash-map
#   NOTE: the given split is sorted, such that a match is order independent
def is_set_tuple(split, occurrence_set):
    return str(sorted(split, reverse=True)) in occurrence_set

#   Checks if the sum of a given tuple is equal to the magic constant, s
def is_valid_tuple(s, split):
    return sum(split) == s


