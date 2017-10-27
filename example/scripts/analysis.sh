#!/usr/bin/env bash
# USAGE: bash analysis.sh
# to produce plots for isles and abyss, as well as an archive of the results.

# Count words
scripts/wordcount.py books/isles.txt isles.tsv
scripts/wordcount.py books/abyss.txt abyss.tsv

# Plot counts
scripts/plotcount.py isles.tsv isles.png
scripts/plotcount.py abyss.tsv abyss.png

# Now archive the results in a tarball so we can share them with a colleague.
rm -rf zipf_results
mkdir zipf_results
mv isles.tsv abyss.tsv isles.png abyss.png zipf_results/
tar -czf zipf_results.tgz zipf_results
rm -r zipf_results
