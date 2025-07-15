##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import glob
import pandas
from functions import send_email
from random import choice

date_now = dt.datetime.now()
date_day = date_now.day
date_month = date_now.month
date_year = date_now.year

letters = glob.glob('letter_templates/*.txt')
# Gets all the txt files in the letter_templates dir

with open("birthdays.csv", "r") as file:
    df = pandas.DataFrame(pandas.read_csv(file))
    result = df[(df['month'] == date_month) & (df['day'] == date_day)]

    for _,row in result.iterrows():
        random_letter = choice(letters)
        name = row['name']
        email = row['email']

        with open(f"{random_letter}","r") as letter:
            letter = letter.read()
            letter = letter.replace("[NAME]",name)
            print(letter)
            send_email(email,letter)