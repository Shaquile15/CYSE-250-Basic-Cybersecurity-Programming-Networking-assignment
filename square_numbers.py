# Read numbers and write their squares
with open("numbers.txt", "r") as infile, open("squares.txt", "w") as outfile:
    for line in infile:
        num = int(line.strip())
        outfile.write(f"{num ** 2}\n")
