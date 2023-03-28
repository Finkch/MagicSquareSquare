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
import magic_utility
import splitting    #   Methods of splitting s into d components
import magic_utility as mu  #   Various handy-dandy functions


#   Checks if the candidate is a magic square
#   TODO: this
#def is_magic_square(s, candidate, splits, squares):


#   Checks if s can create a magic square
def magic_dance(s, candidates, squares, min_squares, occurrence_threshold, split_fxn, d):

    #   Generates the ways to split s into d sums
    #       split_3 is automatically 3 components
    splits = split_fxn(s, squares, min_squares, d)

    #   Prints out a progress update
    if s % 10 == 0:
        print(s, end=" ")

    #   Creates a histogram of integer squares in the tuples
    counts = mu.has_enough_squares(splits, d)


    #   Removes tuples that don't exclusively contain values that
    #   occur a sufficient number of times to potentially create a
    #   magic square. However, it's just too inefficient, so we skip
    #   it most of the time
    """
    if occurrence_threshold > 1:
        #   Trims unnecessary tuples
        splits = mu.count_occurrences(splits, s, occurrence_threshold)
    """

    #   Calculates the integer root sums of each tuple
    root_sums = []
    for i in splits:
        root_sums.append([squares[j] for j in i[:-1]])
        root_sums[-1].append(sum(root_sums[-1]))


    #   Couples each split with its root equivalent
    #   The shape of the data is:
    #       [[S, |S|], ..., [[A_i, B_i, ..., D_i, sq_i], [a_i, b_i, ..., d_i, s_i]], ...]
    #   where capitals refer to the squared numbers and lowercase refers to integer roots
    splits = [[splits[i], root_sums[i]] for i in range(len(splits))]

    #   Checks if there is a sufficient amount (2 * d + 2) of root sums with the same sum
    #splits = magic_utility.count_root_sums(splits, s, d)

    #   If this has insufficient number of tuples
    #if len(splits) <= (2 * d + 2):
    #    return

    #   Prefaces the tuple with the sum and the ways to split that sum
    splits.insert(0, [s, len(splits)])


    #   Appends the split to the list of candidates
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
    occurrence_threshold = 1

    #   Prints the startup summary
    print("Checking from ", minimum, " to ", maximum, ", requiring at least ", min_squares, " integer square!", sep="")

    #   An array to quickly lookup square roots
    squares = mu.create_squares(maximum)


    #   The way we'll be splitting s into its d components
    split_fxn = None
    if d == 3:
        split_fxn = splitting.split_3
    elif d == 5:
        #split_fxn = splitting.split_5
        split_fxn = splitting.split_recursive  #   This is faster!


    #   With s = 100...
    #       Without integer squares, len(splits) = 784
    #       With integer squares 1, len(splits) = 264 (roughly 's / log_10(s)')
    #       With integer squares 2, len(splits) = 30
    #       With integer squares 3, len(splits) = 0

    #   Splits s into 3 components
    #       Arrays that pass the checks are placed within the candidates array
    for s in range(minimum, maximum):
        magic_dance(s, candidates, squares, min_squares, occurrence_threshold, split_fxn, d)

    #   Prints out the list of integer squares computed
    print("\nSquares:", squares, "\n")

    #   Lists out all candidates
    for i in candidates:
        print(i)

    #   Prints the count of candidates
    print("\nNumber of candidates:", len(candidates))


main()