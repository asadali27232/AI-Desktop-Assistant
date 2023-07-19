import pypandoc
from modules.Sayer import Sayer
from modules.Listener import Listener
from modules.SystemQueries import SystemQueries
from modules.WebQueries import WebQueries
from modules.OpenAI import OpenAI

sayer = Sayer()
listener = Listener()
system_queries = SystemQueries()
web_queries = WebQueries()
open_ai = OpenAI()

sayer.say("Hello, I am your personal assistant. How may I help you?")

sayer.say("Listening")
query = listener.listen()
sayer.say("Sure! One moment please.")

query = query.lower()

if "word document" in query:
    sayer.say("Creating a Word Document for you.")
    # Ammend query to force it to write HTML code
    query = query.replace("word document", "Write HTML document code") + "\n\n Write at least 1000+ words as content for the document."

    # Ask OpenAI to write HTML code
    response = open_ai.ask_ChatGPT(query, words=2000)

    # Write HTML code to file
    open("response.html", "w").write("".join(response))

    # Convert HTML to Word Document using Pandoc preserving formatting
    pypandoc.convert_file("response.html", "docx", outputfile="New Document Created by AI.docx")
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
    print(response)
