from telethon import TelegramClient, events, sync
from twilio.rest import Client
from datetime import datetime, timedelta
import os

call1_time = datetime.now() - timedelta(minutes=10)
call2_time = datetime.now() - timedelta(minutes=10)

api_id = ''
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)

account_sid = ''
auth_token = ''
twClient = Client(account_sid, auth_token)

def log(ip):
    print(ip)
    os.system(f'echo "{ip}" >> /home/ubuntu/tele-bot/public/0adb373d-4a4e-48c5-bbaa-df874e3565b8/tele.log')

@client.on(events.NewMessage(chats='H1B_H4_Visa_Dropbox_slots'))
async def my_event_handler(event):
    global call1_time
    global call2_time
    log(datetime.now().strftime("%D %H:%M:%S") + ' ' + event.raw_text)
    if(event.photo):
        log(datetime.now().strftime("%D %H:%M:%S") + ' PIC RECEIVED !!!')
        call_flag = False
        if datetime.now() - call1_time > timedelta(minutes=5):
            call_flag = True
            call1_time = datetime.now()
        elif datetime.now() - call2_time > timedelta(minutes=5):
            call_flag = True
            call2_time = datetime.now()

        if call_flag:
            call = twClient.calls.create(
                                twiml='<Response><Say>Hari, Visa drop box appointment available, please book as soon as possible </Say></Response>',
                                to='',
                                from_=''
                            )
            log(datetime.now().strftime("%D %H:%M:%S") + ' Calling Hari ' + call.sid)
            call = twClient.calls.create(
                                twiml='<Response><Say>Tamil, Visa drop box appointment available, please book as soon as possible </Say></Response>',
                                to='',
                                from_=''
                            )
            log(datetime.now().strftime("%D %H:%M:%S") + ' Calling Tamil ' + call.sid)
        else:
            log(datetime.now().strftime("%D %H:%M:%S") + ' Calling not done')

client.start()
client.run_until_disconnected()



