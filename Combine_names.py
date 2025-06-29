# Combine first and last names
with open("first_names.txt", "r") as fnfile, open("last_names.txt", "r") as lnfile, open("full_names.txt", "w") as outfile:
    for first, last in zip(fnfile, lnfile):
        full_name = f"{first.strip()} {last.strip()}"
        print(full_name)
    
        outfile.write(full_name + "\n")
