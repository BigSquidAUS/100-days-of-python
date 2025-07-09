#List Comprehension Exercises
#Generate a list of the squares of numbers from 1 to 10. eg [1,4,9,16.....etc]
squares = [num * num for num in range(1,101)]
print(squares)

#Create a list of even numbers between 1 and 20.
even = [num for num in range(1,21) if num % 2 == 0]
print(even)

#Given a list of words:
words = ["apple","banana","cherry","date"]
#Use a comprehension to create a list of the lengths of each word.
word_lengths = [len(word) for word in words]
print(word_lengths)

#Write a list comprehension that takes a string and removes all the vowels.
the_input = "Hello world"
output = [letter for letter in the_input if letter not in ["a","e","i","o","u"]]
print(output)

#Flatten a 2D list, flatten this nested list into a 1D list:
matrix = [[1,2],[3,4],[5,6]]
output = [num for sublist in matrix for num in sublist]
#This is a nested comprehension, which works like nested loops
#Each num is pulled from the inner lists (sublist), and all are gathered into one list.
print(output)