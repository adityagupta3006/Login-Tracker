from twilio.rest import Client
import datetime
import sys
now = str(datetime.datetime.now())
date = now[:10]
time = now[-15:-7]
text = "Hi Aditya, your computer was accessed on " + date + " at " + time + "."
client = Client("accountSID", "authToken")
client.messages.create(from_='your_twilio_number_here', to='SMS_recepient_here', body=text)
sys.exit()