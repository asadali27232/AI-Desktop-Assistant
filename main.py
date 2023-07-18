from modules.Sayer import Sayer
from modules.Listener import Listener
from modules.SystemQueries import SystemQueries
from modules.WebQueries import WebQueries
from modules.OpenAI import OpenAI
from modules.SoundPlayer import SoundPlayer

sayer = Sayer()
listener = Listener()
system_queries = SystemQueries()
web_queries = WebQueries()
open_ai = OpenAI()
sound_player = SoundPlayer()

sayer.say("Hello, I am your personal assistant. How may I help you?")

sayer.say("Listening")
query = listener.listen()

query = query.lower()

if "word document" in query:
    query = query.replace("word document", "Write HTML document code")
    print(query)
elif "open" in query:
    check_system = system_queries.execute_command(query)
    check_web = web_queries.open_site(query)

    if check_web != False:
        sayer.say(check_web)
    elif check_system != False:
        sayer.say(check_system)
    else:
        sayer.say("System: Sorry, I didn't get that.")
else:
    response = open_ai.ask_ChatGPT(query, words=100)
    sayer.say(response)
