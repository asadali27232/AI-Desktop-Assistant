from Sayer import Sayer
from Listener import Listener
from SystemQueries import SystemQueries
from WebQueries import WebQueries

sayer = Sayer()
listener = Listener()
system_queries = SystemQueries()
web_queries = WebQueries()

sayer.say("Hello, I am your personal assistant. How may I help you?")

query = listener.listen()

query = query.lower()

system_queries.execute_command(query)
web_queries.open_site(query)
