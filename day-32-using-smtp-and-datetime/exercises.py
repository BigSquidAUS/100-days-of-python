import os
import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
day_of_the_week = now.weekday()

with open("quotes.txt", "r") as quotes:
    quote_list = quotes.readlines()
    the_quote = choice(quote_list)
    print(the_quote)


if day_of_the_week == 0: #If it is Monday (eg: 0)
    #Make sure SMTP details are set in your Python Environmental Variables.
    host = os.getenv("SMTP_SERVER")
    user_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PW")
    recipient = "ben.scholz86@gmail.com"
    msg = "Subject: Your Monday Motivation\n\n"
    msg += the_quote

    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(user_email,password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=recipient,
            msg=msg,
        )
else:
    print("It's not Monday.")