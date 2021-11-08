import os
from dotenv import load_dotenv
import time
from twilio.rest import Client


class IvrTester:
    load_dotenv()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    phone_number = os.environ['TWILIO_PHONE_NUMBER']
    client = Client(account_sid, auth_token)
    current_call_sid = None
    voice_type = 'Polly.Joanna'

    """
        make_call
        
        Uses twilio's api to make a call. Does not finish function
        until the call is connected, canceled, busy, no-answer, or failed
    """
    def make_call(self, from_address, to_address):
        self.current_call_sid = self.client.calls.create(url=os.environ["NGROK_URL"],
                                                         to=to_address,
                                                         from_=from_address).sid
        unanswered = True

        completed_statuses = ['canceled', 'completed', 'busy', 'no-answer', 'failed', 'in-progress']

        while unanswered:
            time.sleep(0.5)
            status = self.client.calls(self.current_call_sid).fetch().status
            if status in completed_statuses:
                unanswered = False

        return self.current_call_sid
