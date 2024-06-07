import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

auth_token = os.getenv("AUTH_TOKEN")
account_sid = os.getenv("ACC_SID")

client = Client(account_sid=account_sid,
                auth_token=auth_token,
                region='au1',
                edge='sydney')
# do we use roaming?

to_number = '0501234567' # placeholder
from_number = '0507654321' # twilio phone numnber goes here
message_body = 'Hello from Twilio!' # placeholder

# input validation for to_number?

message = client.messages.create(to=to_number,
                           from_=from_number,
                            status_callback='',
                        body=message_body)
