import os
from twilio.rest import Client

sms_para_amigos = 'Novo programador na área'
if('sms_para_amigos'):
   print('Novo programador na área!')  

account_sid ="AC266eafc7aa1e7f63173d1d3ac3df5a35"
auth_token ="620deaed556dc0cf342ca7e83c57d674"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="NOVO PROGRAMADOR NA ÁREA!",
                     from_='+17795480749',
                     to='+55(numero pessoasl'
                 )

print(message.sid)
