#Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Initialise an empty list to hold all the invited names.
name_list = []
PLACEHOLDER = "[name]"

# Open the file containing the list of invitee names.
with open("Input/Names/invited_names.txt") as file_names:
    # Read each line from the file.
    for name in file_names.readlines():
        # Remove any leading/trailing whitespace (like newline characters).
        name = name.strip()
        # Add the cleaned name to the name_list.
        name_list.append(name)

with open("Input/Letters/starting_letter.txt") as letter_template:
    template_contents = letter_template.read()

    for name in name_list:
        new_letter = template_contents.replace(PLACEHOLDER,name)
        with open(f"Output/ReadyToSend/Letter for {name}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)