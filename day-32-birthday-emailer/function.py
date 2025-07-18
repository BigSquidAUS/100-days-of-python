import os
import smtplib

def send_email(recipient,message):
    #Make sure SMTP details are set in your Python Environmental Variables.
    host = os.getenv("SMTP_SERVER")
    user_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PW")
    msg = "Subject: Happy Birthday!\n\n"
    msg += message

    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(user_email,password)
        connection.sendmail(user_email,recipient,msg)