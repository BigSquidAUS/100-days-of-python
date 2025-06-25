dir = ""

with open(f"{dir}the_file.txt",mode="w") as file:
    # mode = "w" opens the file in a writable mode. Overwrites content.
    file.write("This is some new text.\n")

with open(f"{dir}the_file.txt",mode="a") as file:
    # mode = "a" opens the file in append mode. Appends existing content.
    file.write("A is for append")

with open(f"{dir}the_file.txt") as file:
    # Using with saves you from needing to file.close() the file when you are done with it.
    # Default mode is r. For read-only.
    contents = file.read()
    print(contents)