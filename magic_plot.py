#   This file handles plotting the data.
#   Plotting is not important to the algorithm or the problem itself.
#       Rather, it is to better visualise the shape of the data to make
#       better assumptions and solutions

import matplotlib.pyplot as plt
import magic_utility as mu

#   Plots the occurrences of each number in splits
def plot_occurrences(splits):

    #   Creates a dictionary of occurrences
    occs = mu.count_occurrences_dict(splits)

    #   Gets the components of the plot
    fig, ax = plt.subplots()

    #   Creates the scatter plot
    ax.scatter(occs.keys(), occs.values())

    #   Shows the plot
    plt.show()
