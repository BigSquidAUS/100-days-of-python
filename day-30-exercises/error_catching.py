#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["i-dont-exist"])
except FileNotFoundError:
    file = open("a_file.txt", "w") # If doesn't exist then the file is created by opening in (w)rite mode.
    file.write("A thing.")
except KeyError as error_message:
    print(f"Dictionary key: {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

