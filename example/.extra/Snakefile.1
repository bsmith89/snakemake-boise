# Dummy Targets
rule all:
    input: "isles.png", "abyss.png"

rule clean:
    shell: "rm --force *.tsv *.png zipf_results.tgz"

# Analysis
rule wordcount_isles:
    input: "books/isles.txt"
    output: "isles.tsv"
    shell: "scripts/wordcount.py books/isles.txt isles.tsv"

rule wordcount_abyss:
    input: "books/abyss.txt"
    output: "abyss.tsv"
    shell: "scripts/wordcount.py books/abyss.txt abyss.tsv"

# Plotting
rule plotcount_abyss:
    input: "abyss.tsv"
    output: "abyss.png"
    shell: "scripts/plotcount.py abyss.tsv abyss.png"

rule plotcount_isles:
    input: "isles.tsv"
    output: "isles.png"
    shell: "scripts/plotcount.py isles.tsv isles.png"

# Deliverables
rule archive_results:
    input: "isles.tsv", "abyss.tsv", "isles.png", "abyss.png"
    output: "zipf_results.tgz"
    shell:
        """
        rm -rf zipf_results/
        mkdir zipf_results
        cp isles.tsv abyss.tsv isles.png abyss.png zipf_results/
        tar -czf zipf_results.tgz zipf_results/
        rm -r zipf_results
        """
