#   This file puts the individual functions together depending on the problem at hand
#   For example, bi_magic_dance called when searching for a bi-magic square

import magic_utility as mu


#   Finds magic square squared
#       That is, magic squares where each item is a distinct integer square
#       However, in the 3x3 case that is impossible with 9 or 8 distinct items
#           So instead we have some min_squares parameter that determines the
#           minimum amount of integer squares that must be within a magic square
def square_magic_dance(s, d, splits, squares, params):
    occurrence_threshold = params[0]

    #   Creates a histogram of integer squares in the tuples
    counts = mu.has_enough_squares(splits, d)

    #   Removes tuples that don't exclusively contain values that
    #   occur a sufficient number of times to potentially create a
    #   magic square. However, it's just too inefficient, so we skip it.
    if occurrence_threshold > 1:

        #   Trims unnecessary tuples
        splits = mu.count_occurrences(splits, s, occurrence_threshold)


    #   If this has insufficient number of tuples
    if len(splits) <= (2 * d + 2):
        return

    #   Prefaces the tuple with the sum and the ways to split that sum
    #   The shape of the data is now...
    #       [[S, | S |], ..., [[A_i, B_i, ..., D_i, sq_i], [a_i, b_i, ..., d_i, s_i]], ...]
    splits.insert(0, [s, len(splits)])

    #   Returns the splits after some processing
    return splits


#   The magic dance for a bi-magic square
#   A bi-magic square is one where each item is a distinct integer square (with magic number S_1)
#       AND each item can be an integer square root (with magic number S_2)
def bi_magic_dance(s, d, splits, squares, params):

    #   Calculates the integer root sums of each tuple
    root_sums = []
    for i in splits:
        root_sums.append([squares[j] for j in i[:-1]])
        root_sums[-1].append(sum(root_sums[-1]))


    #   Couples each split with its root equivalent
    #   The shape of the data is:
    #       [..., [[A_i, B_i, ..., D_i, sq_i], [a_i, b_i, ..., d_i, s_i]], ...]
    #   where capitals refer to the squared numbers and lowercase refers to integer roots
    splits = [[splits[i], root_sums[i]] for i in range(len(splits))]

    #   Checks if there is a sufficient amount (2 * d + 2) of root sums with the same sum
    splits = mu.count_root_sums(splits, s, d)

    #   If this has insufficient number of tuples
    if len(splits) <= (2 * d + 2):
        return

    #   Has the same shape as candidates, so a series of tuples with the shape of splits
    #   Tuples of...
    #       [[S, | S |], ..., [[A_i, B_i, ..., D_i, sq_i], [a_i, b_i, ..., d_i, s_i]], ...]
    root_splits = mu.decouple_over_root_sum(splits, s)

    return root_splits
