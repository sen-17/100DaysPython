import smtplib
import random
import pandas as pd
import datetime as dt
import pytz

# Paths
birth_data = r"day-32\birthday-wish-project\birthday_data\Birthday Date - Sheet1 (1).csv"
letter_template_1 = r"day-32\birthday-wish-project\letters\letter_1.txt"
letter_template_2 = r"day-32\birthday-wish-project\letters\letter_2.txt"
letter_template_3 = r"day-32\birthday-wish-project\letters\letter_3.txt"
letter_templates = [letter_template_1, letter_template_2, letter_template_3]

# Email and Pass
my_email = "urbestpren@gmail.com"
password = "mmmdnvdvtngcuajt"

# Get Date
tz_NY = pytz.timezone('Asia')
today = dt.datetime.now(tz_NY)
today_day = today.day
today_month = today.month

# get data
data = pd.read_csv(birth_data)
data["Birth Date"] = pd.to_datetime(data["Birth Date"]) # convert to date time

# get birthday person row
birthday_people = data[
    (data["Birth Date"].dt.month == today_month) &
    (data['Birth Date'].dt.day == today_day)
]

# send email function
def send_email(friends_email , subject , body):
    message = f"Subject:{subject}\n\n{body}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password = password)
        connection.sendmail(from_addr=my_email, to_addrs= friends_email, msg=message.encode("utf-8"))

# check if theres someone's bithday
if not birthday_people.empty:
    for index , person in birthday_people.iterrows():
        name = person["Name"]
        friends_email = person["Email"]

        # pick random letter template
        random_letter = random.choice(letter_templates)

        # open random template
        with open(random_letter, mode="r") as file:
            content = file.read()

        # split subject and body
        lines = content.split("\n", 1)
        subject_line = lines[0]
        body = lines[1]

        subject = subject_line.replace("{name}", name)
        body = body.replace("{name}", name)

        send_email(friends_email, subject , body)
        print(f"Sent birthday email to {name} at {friends_email}")
else:
    print("No birthdays today.")









        







