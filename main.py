import os
import requests
import smtplib

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
email1 = os.environ.get("EMAIL1")
app_id=os.environ.get("W_ID")

parameters = {
    'lat':33.582846,
    "lon":72.987385,
    'appid':app_id,
    'cnt':4
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast?'
                        ,params=parameters)

response.raise_for_status()
print(response.status_code)

weather_data = response.json()
is_raining = False

for data in weather_data['list']:
    wd = data['weather'][0]['id']
    if int(wd) < 700:
        is_raining=True

if is_raining:
    with smtplib.SMTP("smtp.gmail.com",port=587) as smp:
        smp.starttls()
        smp.login(user=email,password=password)
        smp.sendmail(from_addr=email,to_addrs=email1,msg ="Subject: Rain \n\n It's raining, Bring an Umbrella")
