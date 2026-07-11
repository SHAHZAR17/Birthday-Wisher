# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import os
import pandas
import datetime as dt
import random
import smtplib

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


bd_wish = pandas.read_csv('birthdays.csv')

birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in bd_wish.iterrows()
}
if __name__ == "__main__":
    today = dt.datetime.now()
    date = (today.month,today.day)
    
    # for row in birthdays_dict.values():
    #     if date == (row['month'],row['day']) :
    if date in birthdays_dict:
        birthdays_person = birthdays_dict[date]
    
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter:
            let = letter.read()
            name = birthdays_person['name']
            email = birthdays_person['email']
            bd_letter = let.replace('[NAME]',name)
    
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f'Subject:Birthday Mail\n\n{bd_letter}')
    
    
