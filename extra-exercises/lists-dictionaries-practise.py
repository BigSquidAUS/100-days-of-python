# Creating and Accessing a List

# Create a list of 5 fruits
fruits = ["Apple","Pear","Orange","Banana","Tomato"]
# Print the first fruit
print(fruits[0])
# Print the last fruit
print(fruits[-1])
# Print the number of fruits in the list.
print(len(fruits))

# Modifying a List
# Start with this list:
animals = ["cat","dog","rabbit"]
# Add Parrot to the end.
animals.append("parrot")
#Remove dog.
animals.remove("dog")
#Insert "hamster" at the second position.
animals.insert(1,"hamster")
#Print the updated list.
print(animals)

#------------------------------------------------------------------------#

#Creating and Accessing a Dictionary

#Create a dictionary representing yourself.
my_info = {
    "name": "Bob",
    "age" : 34,
    "location": "Somewhere out there."
}

#Print your name and location
print(my_info["name"])
print(my_info["location"])

#Add a new key "profession"
my_info["profession"] = "Web Designer"

#Change your age
my_info["age"] = 35

#Delete the location key
del my_info["location"]

#Print the updated dictionary.
print(my_info)

#------------------------------------------------------------------------#

# List of numbers

# Create a list of numbers from 1 to 10.
numbers = []
for i in range(1,11):
    numbers.append(i)

#Print all the even numbers
for i in numbers:
    if i % 2 == 0:
        print(i)

#Print the sum of the numbers
print(sum(numbers))

#Print the list in reverse
print(numbers[::-1]) #Slicing operator.
# OR
numbers.reverse() #Reverse method
print(numbers)

#------------------------------------------------------------------------#

# Dictionary of lists

#Create a dictionary where each key is a day of the week, and the value is a list of tasks.
schedule = {
    "Monday":["Emails","Meeting","Do dishes","Do washing"],
    "Tuesday":["Web Design","Gym"],
    "Wednesday":["Client Call"]
}

#Add "Backup" to Wednesday's task list.
schedule["Wednesday"].append("Backup")

#Print all tasks for Tuesday.
print(schedule["Tuesday"])

#Add a new day with tasks.
schedule["Thursday"] = ["Run around the block", "Feed Guinea Pigs", "Some other task."]

#Print all days alongside their number of tasks.
for day, tasks in schedule.items():
    print(f"{day}: {len(tasks)}")

#------------------------------------------------------------------------#

#List of dictionaries

#Create a list of dictionaries, each representing a book with "title", "author", "year".
books = [
        {"title":"1984","author":"George Orwell","year":1949},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953},
        {"title":"To Kill a Mockingbird","author":"Harper Lee","year":1960},
        {"title":"The Great Gatsby","author":"F. Scott Fitzgerald","year":1925},
        {"title":"Catch-22","author":"Joseph Heller","year":1961},
        {"title":"Slaughterhouse-Five","author":"Kurt Vonnegut","year":1969},
        {"title":"Animal Farm","author":"George Orwell","year":1945},
        {"title":"Lord of the Flies","author":"William Golding","year":1954},
        {"title":"One Flew Over the Cuckoo's Nest","author":"Ken Kesey","year":1962},
        {"title":"The Catcher in the Rye","author":"J.D. Salinger","year":1951},
        {"title":"A Clockwork Orange","author":"Anthony Burgess","year":1962}
         ]

#Print all the book titles.
for i in books:
    print(i["title"])

#Print the title of the most recent book.
book_year = 0
latest_book = None
for i in books:
    if i["year"] > book_year:
        latest_book = i["title"]
print(f"The most recently published book is: {latest_book}")

#Add a new book to the list
books.append({"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937})

#Print book with specific title
for book in books:
    if book["title"] == "Animal Farm":
        print(book)

#------------------------------------------------------------------------#

#Student Grades tracker

#Create a dictionary of students and their scores.
grades = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 67,
    "David": 72,
    "Eva": 91,
    "Frank": 54,
    "Grace": 77,
    "Liam": 11,
    "Mia": 90,
    "Nathan": 55,
    "Olivia": 99
}

#Increase Alice's score by 5.
grades["Alice"] += 5

#Remove Charlie
del grades["Charlie"]

#Add a new student, "Diana", with a score of 91.
grades["Diana"] = 91

#Print each student with a label of Pass/Fail (Passing score is > 70)
for student,score in grades.items():
    if score > 70:
        print(f"{student} : PASS ({score})")
    else:
        print(f"{student} : FAIL ({score})")

#------------------------------------------------------------------------#

#Inventory Manager

#Write a function that takes an inventory dictionary like this.
inventory = {
    "laptops":5,
    "monitors":3,
    "keyboards":0,
}

#The function will: 1. Print each item and its quantity. 2. Add a new item to the inventory. (eg "mice":4).
# 3. Subtract 1 from "laptops". 4. Remove any item that has a quantity of 0.
def manage_inventory(inv_dict):
    inv_dict["mice"] = 4 #2. Add a new item to the inventory. (eg "mice":4).
    inv_dict["laptops"] -= 1 #3. Subtract 1 from "laptops".

    for item in list(inv_dict.keys()): #4. Remove any item that has a quantity of 0.
        if inv_dict[item] == 0:
            del inv_dict[item]

    #Important Note: list() is used to create a "copy" of the dictionary keys.
    #Python dictionaries don't allow structural changes during iteration so a copy is used.
    #By using list() you are iterating over this "safe snapshot", not the live dictionary.
    #Now it is safe to modify the ACTUAL dictionary during the loop.


    for item,qty in inv_dict.items(): # 1. Print each item and its quantity.
            print(f"{item} | Quantity: {qty}")

manage_inventory(inventory)