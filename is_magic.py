#   These functions check whether a split is able to form a magic square

import magic_utility as mu

#   Checks whether a split can make a boring, regular magic square
def is_magic_square(s, d, splits, squares, params):

    #   Obtains a dictionary that maps a number that appears in splits to
    #   all tuples in which that number makes an appearance.
    occs = mu.create_occurrences_dictionary(splits)

    #   ...How do I actually check whether it's magic? Like, without permutations?



    return

#   Checks whether a split can make a bi-magic square
#   As a reminder, a bi-magic square...
#       Has dxd distinct integers that sum to S_1
#       The square of those dxd distinct integer squares sum to S_2
def is_bi_magic_square(s, d, root_splits, squares, params):
    return