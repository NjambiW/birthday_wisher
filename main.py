import smtplib
import datetime as dt
import pandas
import random

PLACEHOLDER = "[NAME]"
my_email = "wambuibennahnjambi@yahoo.com"
password = "20172017"

# check today matches a birthday in the birthdays
birthday = dt.datetime.now()
birth_month = birthday.month
birth_day = birthday.day
today = (birth_month, birth_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
file_path = f"letter_{random.randint(1,3)}.txt"

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(file_path) as file:
        letter_contents = file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, birthday_person["name"])
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection = connection.sendmail(from_addr=my_email,
                                             to_addrs=birthday_person["email"],
                                             msg=f"subject: HAPPY BIRTHDAY\n\n{new_letter}")
    print("false")


