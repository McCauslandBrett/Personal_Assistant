import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

phone_book = {}
phone_book['Terry'] = '19498807364'

call_reciever = 'Terry'

account_sid = 'AC1638427d68b93fd34df43a6d48cc582e'
auth_token ='8e747f33010216272f418c3931786267'
client = Client(account_sid, auth_token)


outgoing_number= phone_book[call_reciever]

message = client.messages \
                .create(
                     body="Hi",
                     from_='+19728939499',
                     to=outgoing_number
                 )
