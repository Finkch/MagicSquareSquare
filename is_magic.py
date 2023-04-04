#   These functions check whether a split is able to form a magic square

import magic_utility as mu

#   Checks whether a split can make a boring, regular magic square
#   TODO: this
def is_magic_square(s, d, splits, squares, params):

    #   Removes items that describe the shape
    splits = [i[:-1] for i in splits[1:]]

    #   Obtains a dictionary that maps a number that appears in splits to
    #   all tuples in which that number makes an appearance.
    occs = mu.create_occurrences_dictionary_unshaped(splits)

    #for i in splits:
    #    is_magic_square_3(i, occs)

    candidiates = is_magic_square_set_3(d, splits, occs)


    for i in candidiates:
        print(i)

    print(len(candidiates))


#   Creates all unique trios of tuples
def is_magic_square_3(tuples, occs):
    candidates = []

    for i in occs[tuples[0]]:
        for j in occs[tuples[1]]:
            for k in occs[tuples[2]]:
                if mu.is_unique_tuple(i, j) and mu.is_unique_tuple(j, k):
                    candidates.append([i, j, k])

    return candidates


#   TODO:
#       Create a recursive function that chooses 2 * d + 2 tuples from splits.
#       Do so intelligently, only adding tuples which contain at least one key from the previous.
#       Then do the counting game?
#       Alternatively, do the counting game as we add them such that only good arrays may be added;
#       thus, if we add the '2 * d + 2'-th item, we have a good array.
#
#       Hm, how about choose d tuples with unique elements.
#       Then, add more tuples iff they don't have unique elements.
#       Keep choosing these tuples until 2 * d + 2 tuples have been chosen
def is_magic_square_set_3(d, splits, occs):
    candidates = []

    for i in splits:
        is_magic_square_set_setup(d, i, occs, candidates)

    #for i in candidates:
    #    print(i)

    #print("Len:", len(candidates))

    return candidates

#   TODO:
#       Improve the creation of the unique set such that duplicate unique sets
#       aren't checked. In other words, iterate over the unique set of unique sets.
#       Using recursion and pass down the trimmed set (like the recursive square split).
#       Effectively ensuring that 'a > b > c' by passing 'splits[a:]'.
def is_magic_square_set_setup(d, tuples, occs, candidates):

    for i in occs[tuples[0]]:
        for j in occs[tuples[1]]:
            for k in occs[tuples[2]]:
                if mu.is_unique_tuple(i, j) and mu.is_unique_tuple(j, k) and mu.is_unique_tuple(i, k):
                    unique_tuple = [i, j, k]

                    unique_set = set()
                    for l in unique_tuple:
                        unique_set.update(l)

                    #   For this unique set, add the remaining necessary tuples
                    #       The 'd + 2' arises from '(2 * d + 2) - d = d + 2' since we've
                    #       already chosen d tuples to create the unique set.
                    is_magic_square_set_step(d + 2, occs, unique_tuple, unique_set, [], candidates)


def is_magic_square_set_step(depth, occs, unique_tuples, unique_set, non_unique_tuples, candidates):

    if depth == 0:
        candidates.append([unique_tuples, non_unique_tuples])
        #is_magic_square_step_count(3, unique_tuples, non_unique_tuples, candidates)
        return

    #   Not sure about this
    if len(unique_set) < depth:
        return

    non_unique_tuples.append([])

    #   This _horrendous_ thing worked first try.
    #       I'm not sure whether I should be amazed or terrified.
    for i in unique_set:    #   Iterates over the unique sets
        for j in occs[i]:   #   Iterates over all occurrences of that item in occs

            #   Ensures that this tuples has not yet been considered AND all its
            #   elements are within the unique-set (it's entirely non-unique).
            if j not in unique_tuples and j not in non_unique_tuples and mu.only_contains_non_unique(unique_set, j):
                #   Updates the candidates tuples to include the newest candidate
                non_unique_tuples[-1] = j

                #   Recurse
                #       Not the unique_set: it trims the set such that it doesn't include
                #       the current i being considered.
                #   TODO: don't just remove the one i, remove all previous i's
                is_magic_square_set_step(depth - 1, occs, unique_tuples, set([l for l in unique_set if l != i]), non_unique_tuples.copy(), candidates)


def is_magic_square_step_count(d, unique_tuples, non_unique_tuples, candidates):
    counts = {}

    #   Fills the counts dictionary
    is_magic_count(unique_tuples, counts)
    is_magic_count(non_unique_tuples, counts)

    #   For d = 3
    t = [4, 3, 3, 3, 3, 2, 2, 2, 2]

    check = [i for i in counts.values()]
    check.sort(reverse=True)

    #print(check)
    #   Checks if the counts fulfills the conditions
    if mu.equivalent_tuple(t, check):
        candidates.append([unique_tuples, non_unique_tuples])
        #   If so, adds it to the candidates array


def is_magic_count(arr, counts):
    for i in arr:
        for j in i:
            if j not in counts.keys():
                counts[j] = 0
            counts[j] += 1


#   This approach does select all combinations of 8 tuples, but not a good approach
def is_magic_square_recursive(d, splits, occs):
    candidates = []

    for i in splits:
        is_magic_square_recursive_step(d, occs, 2 * d + 2, [i], candidates)

    return candidates

def is_magic_square_recursive_step(d, occs, depth, cur, candidates):

    #   Base case
    if depth == 0:

        candidates.append(cur)
        return

    cur.append([])

    for i in cur[-2]:
        for j in occs[i]:

            if j not in cur:

                cur[-1] = j
                is_magic_square_recursive_step(d, occs, depth - 1, cur.copy(), candidates)


#   Uses an inefficient approach from a previous version
#   TODO: this
def is_magic_square_permutations(s, d, splits, squares, params):

    return


#   Checks whether a split can make a bi-magic square
#   As a reminder, a bi-magic square...
#       Has dxd distinct integers that sum to S_1
#       The square of those dxd distinct integer squares sum to S_2
#   TODO: this
def is_bi_magic_square(s, d, root_splits, squares, params):
    return