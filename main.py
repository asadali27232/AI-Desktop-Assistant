from Sayer import Sayer
from Listener import Listener
from SystemQueries import SystemQueries
from WebQueries import WebQueries
from OpenAI import OpenAI

sayer = Sayer()
listener = Listener()
system_queries = SystemQueries()
web_queries = WebQueries()
open_ai = OpenAI()

sayer.say("Hello, I am your personal assistant. How may I help you?")

query = listener.listen()

query = query.lower()
print("You said:", query)

if "open" in query:
    check_system = system_queries.execute_command(query)
    check_web = web_queries.open_site(query)

    if check_web != False:
        sayer.say(check_web)
    elif check_system != False:
        sayer.say(check_system)
    else:
        sayer.say("System: Sorry, I didn't get that.")
else:
    # open_ai.ask_ChatGPT(query)
    pass