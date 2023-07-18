from Sayer import Sayer
from Listener import Listener
from SystemQueries import SystemQueries
import webbrowser

sayer = Sayer()
listener = Listener()
system_queries = SystemQueries()

sayer.say("Hello, I am your personal assistant. How may I help you?")

query = listener.listen()

query = query.lower()
if "open youtube" in query:
    webbrowser.open("youtube.com")


system_queries.process_query(query)
