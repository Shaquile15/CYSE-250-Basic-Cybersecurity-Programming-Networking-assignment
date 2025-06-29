# Duplicate lines from input to output using original line endings
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line)
        outfile.write(line)
