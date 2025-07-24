import smtplib
import random
import datetime as dt

data_path = r"day-32\email-quote-project\quotes.txt"
my_email = "urbestpren@gmail.com"
password = "mmmdnvdvtngcuajt"

with open(data_path, mode="r") as file:
    data = [line.strip() for line in file]

random_quote = random.choice(data)

now = dt.datetime.now()
check_day = now.weekday()

if check_day == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, to_addrs="jassonjasson17@gmail.com", msg =f"Subject: Monday Motivation\n\n{random_quote}")
    