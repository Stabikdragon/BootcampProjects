
import pandas, random, datetime, smtplib

user = "sthomas2357@gmail.com"
password = "iikzytnkyiwqeqzz"

now = datetime.datetime.now()
today = (now.month, now.day)

birthday_frame = pandas.read_csv("birthdays.csv")



letter_1 = open("letter_templates/letter_1.txt")
letter_2 = open("letter_templates/letter_2.txt")
letter_3 = open("letter_templates/letter_3.txt")
list_of_letter = [letter_1, letter_2, letter_3]

random_letter = random.choice(list_of_letter).read()


def send_email(letter, email):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=user, password=password)
    connection.sendmail(from_addr=user, to_addrs=email, msg=f"Subject:HAPPY BIRTHDAY!\n\n{letter}")

for(index,row) in birthday_frame.iterrows():
    date = (row.month, row.day)
    email = row.email
    if date == today:
        name = row["name"]
        new_letter = random_letter.replace("[NAME]", name)
        send_email(new_letter, email)
        print(new_letter)











