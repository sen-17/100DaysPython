import smtplib

# my_email = "urbestpren@gmail.com"
# password = "mmmdnvdvtngcuajt"

# with smtplib.SMTP("smtp.gmail.com") as connection: #SMTP Information
#     connection.starttls()
#     connection.login(user= my_email, password= password)
#     connection.sendmail(from_addr=my_email, to_addrs="jassonjasson17@gmail.com", msg="Subject:Happy Birthday\n\nHappy Birthday!!!")

import datetime as dt

now = dt.datetime.now()
year = now.year # current year
month = now.month # current month
day = now.day # current day

day_of_week = now.weekday() # 0 - 6 (0 = Monday)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
print(year)