#   These functions check whether a split is able to form a magic square

import magic_utility as mu

#   Checks whether a split can make a boring, regular magic square
#   TODO: this
def is_magic_square(s, d, splits, squares, params):

    #   Removes items that describe the shape
    splits = [i[:-1] for i in splits[1:]]

    #   Obtains a dictionary that maps a number that appears in splits to
    #   all tuples in which that number makes an appearance.
    #occs = mu.create_occurrences_dictionary_unshaped(splits)

    t = mu.create_occurrence_set(splits)

    #for i in splits:
    #    if not mu.is_set_tuple(i, t):
    #        print("False!")

    #print(t)

    #for i in splits:
    #    print(i)

