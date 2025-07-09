# Dictionary Comprehensions Exercise
#Generic Example: {key_expression: value_expression for item in iterable}

#Squares as a dictionary - create a dictionary where the keys are numbers from 1 to 5 and the values are
#their squares. eg {1:1, 2:4, 3:9, 4:16, 5:25...etc}
squares_dict = {num : (num * num) for num in range(1,6)}
print(squares_dict)

#Uppercase Names - Create a dictionary where keys are names, and values are uppercase versions.
names = ["ben","georgia","alice","sam"]
uc_names = {name : name.upper() for name in names}
print(uc_names)

#Filter Scores - given a dictionary of student scores:
scores = {"Alice": 85, "Bob": 42, "Charlie": 78, "Diana": 60,"Smith": 61,}
#Use a dictionary comprehension to keep only students who passed (score > 60).

#new_dict = {key: value for key, value in old_dict.items() if condition}
passed = {name : score for name, score in scores.items() if score > 60}
print(passed)

#Invert a dictionary - invert a dictionary so that values become keys and keys become values.
animal_sounds = {
    "dog": "bark",
    "cat": "meow",
    "cow": "moo"
}
inverted_dict = {key : value for value, key in animal_sounds.items()}
print(inverted_dict)

#Combine two lists into a Dict - given two lists:
keys = ["id", "name", "email"]
values = [1, "Ben", "ben@example.com"]
#Create a dictionary using a comprehension.
a_dictionary = {key : value for key, value in zip(keys,values)}
#Key takeaway: When combining two lists use zip().

#Reverse the process - given:
#a_dictionary = {'id': 1, 'name': 'Ben', 'email': 'ben@example.com'}
#Create a list of keys, create a list of values.
keys = [key for key in a_dictionary.keys()]
print(keys)
values = [value for value in a_dictionary.values()]
print(values)