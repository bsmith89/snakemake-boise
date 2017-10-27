#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
from collections import Sequence

from wordcount import load_word_counts


def plot_word_counts(counts, limit=10):
    """
    Given a list of (word, count, percentage) tuples, plot the counts as a
    histogram. Only the first limit tuples are plotted.
    """
    plt.title("Word Counts")
    limited_counts = counts[0:limit]
    word_data = [word for (word, _, _) in limited_counts]
    count_data = [count for (_, count, _) in limited_counts]
    positions = range(len(word_data))
    width = 1.0
    ax = plt.axes()
    ax.set_xticks([p + (width / 2) for p in positions])
    ax.set_xticklabels(word_data)
    plt.bar(positions, count_data, width, color='b')


def get_ascii_bars(values, truncate=True, maxlen=10, symbol='#'):
    maximum = max(values)
    if truncate:
        minimum = min(values) - 1
    else:
        minimum = 0
    prop_values = [(val - minimum) / (maximum - minimum) for val in values]
    biggest_bar = symbol * round(maxlen / len(symbol))
    bars = [biggest_bar[:round(frac * len(biggest_bar))] for frac in prop_values]
    return bars


def typeset_labels(labels=None, gap=2):
    if not isinstance(labels, Sequence):
        labels = range(labels)
    labels = [str(i) for i in labels]
    label_lens = [len(s) for s in labels]
    label_width = max(label_lens)
    output = []
    for label in labels:
        label_string = label + ' ' * (label_width - len(label)) + (' ' * gap)
        output.append(label_string)
    assert len(set(len(s) for s in output)) == 1
    return output


def plot_ascii_bars(values, labels=None, screenwidth=80, gap=2, truncate=True):
    if not labels:
        try:
            values, labels = zip(*values)
        except TypeError:
            labels = len(values)
    labels = typeset_labels(labels=labels, gap=gap)
    bars = get_ascii_bars(values, maxlen=screenwidth - gap - len(labels[0]),
                          truncate=truncate)
    return [s + b for s, b in zip(labels, bars)]


if __name__ == '__main__':

    # Read args
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    limit = 10
    if len(sys.argv) > 3:
        limit = int(sys.argv[3])

    # Load data
    counts = load_word_counts(input_file)

    # Plot
    if output_file == 'ascii':
        words, counts, _ = zip(*counts)
        for line in plot_ascii_bars(counts[:limit], words[:limit], truncate=False):
            print(line)
    else:
        plot_word_counts(counts, limit)
        if output_file == "show":
            plt.show()
        else:
            plt.savefig(output_file)
