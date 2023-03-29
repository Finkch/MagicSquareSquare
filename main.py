#   Try 2
#   This algorithm is founded on an observation:
#       If s can create a valid magic array, then splits (an array
#       containing all ways to split s into d elements) itself
#       must contain all 2 * d + 2 sums with d distinct elements.
#       There's no need to choose d tuples then permute the elements
#       within the arrays until a magic array is found.
#   This is the approach:
#       Create an array, splits, that contains all ways to split s into d elements.
#       Searches through splits for 2 * d + 2 tuples that obey these properties (d = 3 case):
#           Four items appear exactly two times in the 8 tuples;
#           Four items appear exactly two three in the 8 tuples; and,
#           One item appears exactly four times in the 8 tuples.
#       In addition:
#           At just about each step, there are checks to discard invalid items.
#           At just about each step, there are constraints to trim the search space.
#           At the beginning, an array is creating to allow quick searches whether an item is a integer square.

import magic_dances
import splitting    #   Methods of splitting s into d components
import magic_utility as mu  #   Various handy-dandy functions
import time


#   Checks if the candidate is a magic square
#   TODO: this
def is_magic_square(s, root_splits, squares):


    return


#   Checks to see in a magic constant can create a magic square
#       First creates all ways to split s into d components (following the conditions)
#       Then processes those 'splits' to cut down search space
#       Finally checks to see if that split can form a magic square
def magic_dance(s, d, squares, candidates, min_squares, split_fxn, magic_fxn, params):

    #   Generates the ways to split s into d sums
    #       split_3 is automatically 3 components
    splits = split_fxn(s, d, squares, min_squares)

    #   Prints out a progress update
    if s % 10 == 0:
        print(s, end=" ")

    #   Processes the splits
    #s, d, splits, squares, params
    splits = magic_fxn(s, d, splits, squares, params)


    #   Checks to see if there are a sufficient count of tuples
    #   Split would return type of None if there wasn't a sufficient amount
    if splits is None:
        return

    #   TODO: create function to check if the split is magic

    #   Adds the splits to the list of candidates
    #   Mostly for the post-search printout
    candidates.append(splits)


#   Gets the ball rolling
#   In general, after some threshold, occurrences become common
#       Where occurrences are splits passing some restrictive condition
#           For example: after 654 with d = 5, occurrences of splits with (2 * d + 2)
#           matching integer root sums becomes very common, with some having candidates
#           with upwards of 80 unique splits past the 900 mark.
#           There, about every other number is candidate
def main():

    #   d, the number of components s will be split into
    #      Note:    55 is the first d = 5 number with 5 square integers [25, 16, 9, 4, 1]
    #               654 is the first d = 5 with (2 * d + 2) = 12 matching integer root sums
    d = 5

    #   The minimum number of integer squares required per tuple
    min_squares = d

    #   The bounds of the search
    maximum = 655
    minimum = 654

    #   An array of all splits that are potential magic squares
    candidates = []

    #   The minimum occurrences of a number in a tuple for a valid tuple
    #       The default is 1, which means that nothing happens
    #       The relevant section of code is commented out, so this doubly does nothing
    occurrence_threshold = 1

    #   Prints the startup summary
    print("Checking from ", minimum, " to ", maximum, " for d = ", d, ", requiring at least ", min_squares, " integer square!", sep="")

    #   An array to quickly lookup square roots
    squares = mu.create_squares(maximum)

    #   The type of magic square we're searching for
    magic_fxn = magic_dances.bi_magic_dance
    #magic_fxn = magic_dances.square_magic_dance

    #   The way we'll be splitting s into its d components
    #split_fxn = splitting.split_recursive
    #split_fxn = splitting.split_3
    #split_fxn = splitting.split_5
    split_fxn = splitting.split_5_squares   #   Faster than recursion!

    #   Starts the timer:
    timer_start = time.time()

    #   With s = 100...
    #       Without integer squares, len(splits) = 784
    #       With integer squares 1, len(splits) = 264 (roughly 's / log_10(s)')
    #       With integer squares 2, len(splits) = 30
    #       With integer squares 3, len(splits) = 0

    #   Splits s into 3 components
    #       Arrays that pass the checks are placed within the candidates array
    for s in range(minimum, maximum):
        magic_dance(s, d, squares, candidates, min_squares, split_fxn, magic_fxn, [occurrence_threshold])

    #   Ends the timer
    timer_end = time.time()

    #   Prints out the list of integer squares computed
    print("\nSquares:", squares, "\n")

    #   Lists out all candidates
    for i in candidates:
        print(i)

    #   Prints the count of candidates
    print("\nNumber of candidates:", len(candidates), "\nTime elapsed:", round(timer_end - timer_start, 3), " s")


main()