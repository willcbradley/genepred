def parse_fasta(file):
    sequence = ""

    with open(file) as f:
        for line in f:
            # remove title line
            if line.startswith(">"):
                continue

            # remove \n from end of remaining lines
            line = line.strip()
            sequence += line

    return sequence

