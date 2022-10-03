from twilio.rest import Client
TWILIO_SID = "ACb52bcdc89677afb4b02d936c851068de"
TWILIO_AUTH_TOKEN = "0597e5ec44d53e4f42fcd798ea4e3803"
TWILIO_VIRTUAL_NUMBER = "+19594008593"
TWILIO_VERIFIED_NUMBER = "+33605663244"

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


