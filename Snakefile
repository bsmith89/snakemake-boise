rule make_pdf:
    input: "{name}.md"
    params:
        fmt = lambda x: {'html': 'html',
                         'pdf': 'latex'}[x.ext]
    output: "{name}.{ext}"
    shell: "pandoc -t {params.fmt} -o {output} {input}"
