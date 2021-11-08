from IvrTester import *

# init TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables
tester = IvrTester()
tester.make_call('+18125877953', '+12678465056')
