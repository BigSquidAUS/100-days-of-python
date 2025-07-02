# EXAMPLE CODE

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row)
    print(row.student)
    print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# END EXAMPLE CODE

# Step 1: Import the pandas library so we can work with CSV files and data tables
import pandas

# TO-DO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame (table-like structure)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame:
# - Loop through each row in the table
# - Use the 'letter' column as the key, and the 'code' column as the value
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# Optional: Print each letter and its corresponding code word for verification
for (index, row) in data.iterrows():
    print(f"{row.letter} : {row.code}")

# TO-DO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    # Ask the user to enter a word; convert it immediately to uppercase so it matches the dictionary keys
    user_input = input("Convert to NATO: ").upper()
    # Convert the word into a list of NATO phonetic code words using a list comprehension:
    # - Loop through each letter in the uppercase user input
    # - Look up the code word for each letter in the nato_dictionary
    # - This assumes all characters are valid keys in the dictionary
    try:
        output_list = [nato_dictionary[letter] for letter in user_input]
    except KeyError as error_message:
        print("Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list) # Print the list of code words

generate_phonetic()