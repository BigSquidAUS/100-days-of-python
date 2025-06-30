student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Step 1: Import the pandas library so we can work with CSV files and data tables
import pandas

# TO-DO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame (table-like structure)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame:
# - Each row has a letter and its corresponding code word
# - This comprehension turns those into key-value pairs
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# Print out each letter and its code to verify the dictionary was created correctly
for (index, row) in data.iterrows():
    print(f"{row.letter} : {row.code}")

# TO-DO 2. Create a list of the phonetic code words from a word that the user inputs.

# Ask the user to type a word to convert into NATO phonetic code
user_input = input("Convert to NATO: ")

# Break the user’s input string into a list of individual letters
letters = [letter for letter in user_input]

# Create a new list of phonetic code words:
# - For each letter, convert it to uppercase
# - If it exists in the dictionary, get its code word and add it to the list
phonetic_list = [nato_dictionary[l.upper()] for l in letters if l.upper() in nato_dictionary]

# Print the final list of code words
print(phonetic_list)
