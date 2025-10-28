import requests
import smtplib
import os
from bs4 import BeautifulSoup

#url="https://appbrewery.github.io/instant_pot/" #Practise URL
url = "https://www.amazon.com.au/TP-Link-AX3000-Wi-Fi-Range-Extender/dp/B0BB79NDS2/ref=sr_1_5?crid=1DK6EA7UMTTYZ&dib=eyJ2IjoiMSJ9.4Nz6IcCr1ndCKAGBrJciBgIeZ9COgMvk9mWCCRIMy55l1VJe4PSx9umYbF9brmfzNedHnVqcjQpvA4pnwohxOcPTZ_KmRixt5a2xQ4TU9uRABTvdq2TqEIW-GEdQY1Wa0pFR8wPbiOt3NGm1KBna0ekOWv0go-u0N2mUP6FnbbPBdp8jd2bOVhSIMEII7Yp8DSmfAk9hWA7OwYXque4QZQMMPBqUPkGyREgmSeYfYffBP4DGycqR1zK9hLoXFTIyldfqUU0tWvR5Ovl_lRiVmYANsbIhFIaktGaK2NotPAQ.e3T1y_mErIWDlohiWxd51bc0crTN9I8i036wzCWpeac&dib_tag=se&keywords=tp-link%2Brange%2Bextender&qid=1761088555&sprefix=tp-link%2Brange%2Bextend%2Caps%2C275&sr=8-5&th=1"
#Live URL ^

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
           'accept-language': 'en-AU,en;q=0.9'}
r = requests.get(url,headers=headers)
#print(r) #Check response from request.

soup = BeautifulSoup(r.text,'html.parser')
price = soup.find(name='span', class_='aok-offscreen')
price = float(price.get_text().split("$")[1])
print(price)

send_mail = True

if price < 100 and send_mail:
    # Make sure SMTP details are set in your Python Environmental Variables.
    host = os.getenv("SMTP_SERVER")
    user_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PW")
    recipient = "ben.scholz86@gmail.com"
    msg = "Subject: Price Scaper Triggered\n\n"
    msg += (f"Your item at {url} is currently selling at or below your target price!\n"
            f"Current Price: ${price}")

    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(user_email, password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=recipient,
            msg=msg,
        )