def parse_gff(file, length):

    annotation = ["N"] * length

    with open(file) as f:
        for line in f:

            if line.startswith("#"):
                continue
        
            fields = line.strip().split("\t")

            if fields[2] == "CDS":
                start = int(fields[3])
                end = int(fields[4])

                for i in range(start - 1, end):
                    annotation[i] = "C"

    return "".join(annotation)
