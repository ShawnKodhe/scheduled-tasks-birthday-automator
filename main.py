##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

from dotenv import load_dotenv
import os

import pandas
import datetime as dt
import smtplib
import random

load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
print(MY_EMAIL)

month_now = dt.datetime.now().month
day_now = dt.datetime.now().day
year_now = dt.datetime.now().year

Birthday_Data = pandas.read_csv(
    "birthdays.csv")
print(Birthday_Data)
print(Birthday_Data.month[0])

if month_now == Birthday_Data.month[1] and day_now == Birthday_Data.day[1] and year_now == Birthday_Data.year[1]:
    with open(
            r"letter_templates/letter_1.txt") as letter:
        letter_contents = letter.read()
        # print(letter_contents)
        new_letter = letter_contents.replace("[NAME]", Birthday_Data.name[1])
        # print(new_letter)

    with open(
            r"letter_templates/letter_2.txt") as letter:
        letter_contents = letter.read()
        # print(letter_contents)
        new_letter2 = letter_contents.replace("[NAME]", Birthday_Data.name[1])
        # print(new_letter2)

    with open(
            r"letter_templates/letter_3.txt") as letter:
        letter_contents = letter.read()
        # print(letter_contents)
        new_letter3 = letter_contents.replace("[NAME]", Birthday_Data.name[1])
        # print(new_letter3)

    letter_array = []
    letter_array.append(new_letter)
    letter_array.append(new_letter2)
    letter_array.append(new_letter3)
    print(letter_array[2])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Birthday\n\n{letter_array[random.randint(0,len(letter_array)-1)]}")

if month_now == Birthday_Data.month[2] and day_now == Birthday_Data.day[2] and year_now == Birthday_Data.year[2]:
    with open(
            r"letter_templates/letter_1.txt") as letter:
        letter_contents = letter.read()
        # print(letter_contents)
        new_letter = letter_contents.replace("[NAME]", Birthday_Data.name[2])
        print(new_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Birthday\n\n{new_letter}")
