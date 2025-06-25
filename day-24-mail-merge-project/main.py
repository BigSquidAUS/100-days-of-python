#Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Initialise an empty list to hold all the invited names.
name_list = []

# Open the file containing the list of invitee names.
with open("Input/Names/invited_names.txt") as file_names:
    # Read each line from the file.
    for name in file_names.readlines():
        # Remove any leading/trailing whitespace (like newline characters).
        name = name.strip()
        # Add the cleaned name to the name_list.
        name_list.append(name)

# Loop through each invited name from the list.
for invited in name_list:
    # Open the template letter file for each name.
    with open("Input/Letters/starting_letter.txt", mode="r") as file_letter:
        # Read the entire contents of the template letter.
        new_letter = file_letter.read()

        # Replace the placeholder "[name]" in the template with the actual name.
        new_letter = new_letter.replace("[name]", invited)

        # Optional: Print the personalised letter to the console.
        print(new_letter)

        # Create a new file with the personalised letter.
        with open(f"Output/ReadyToSend/Letter for {invited}.txt", mode="w") as output_file:
            # Write the personalised letter to the new file.
            output_file.write(new_letter)