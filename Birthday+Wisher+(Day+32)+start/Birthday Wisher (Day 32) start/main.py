from smtplib import *
import datetime
import random
import requests


my_email = "sthomas2357@gmail.com"
py_pass = "iikzytnkyiwqeqzz"
now = datetime.datetime.now()
# birthday = datetime.datetime(year=1989, month=12, day=4)

quotes = open("quotes.txt", "r").readlines()
random_quote = random.choice(quotes)

def send_mail():
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=py_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="sthomas2357@hotmail.com",
                            msg=f"Subject:test\n\n {random_quote}")




if now.weekday() == 5:
    send_mail()
