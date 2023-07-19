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
    query = query.replace("word document", "Write HTML document code") + "\n\n Write at least 5000 words as content for the document. Add some headings, subheadings, and paragraphs and also add table or list if you want."

    # Ask OpenAI to write HTML code
    response = open_ai.ask_ChatGPT(query, words=2000)

    # Write HTML code to file
    open("response.html", "w").write("".join(response))

    # Convert HTML to Word Document using Pandoc preserving formatting
    pypandoc.convert_file("response.html", "docx", outputfile="New Document Created by AI.docx")

elif "code" in query:
    languages_and_exts = {"python": "py", "java": "java", "c": "c", "c++": "cpp", "c plus plus": "cpp", "c#": "cs", "c sharp": "cs", "javascript": "js", "java script": "js", "typescript": "ts", "html": "html", "css": "css", "php": "php", "ruby": "rb", "go": "go", "swift": "swift", "kotlin": "kt", "rust": "rs", "scala": "scala", "perl": "pl", "r": "r", "sql": "sql", "bash": "sh", "powershell": "ps1", "power shell": "ps1", "lua": "lua", "matlab": "m", "fortran": "f90", "haskell": "hs", "dart": "dart", "groovy": "groovy", "type script": "ts", "elixir": "ex", "clojure": "clj", "jsx": "jsx", "tsx": "tsx", "json": "json", "xml": "xml", "yaml": "yaml", "ini": "ini", "toml": "toml", "markdown": "md", "mark down": "md"}

    for language, ext in languages_and_exts.items():
        if language in query:
            code_language = language.upper()
            code_ext = ext.lower()
            break

    sayer.say(f"Creating a {code_language} Code File for you.")

    # Ammend query to force it to write Python code
    query = query.replace("code", f"Just write a {code_language} code") + "\n\n Write at least 5000 words as content for the code file. Add some functions, variables, and loops if you want."

    # Ask OpenAI to write code
    response = open_ai.ask_ChatGPT(query, words=2000)

    # Write Python code to file
    open(f"Code file created by AI.{code_ext}", "w").write(response)

elif "open" in query:
    check_system = system_queries.execute_command(query)
    check_web = web_queries.open_site(query)

    if check_web != False:
        sayer.say(check_web)
    elif check_system != False:
        sayer.say(check_system)
    else:
        sayer.say("Sorry, I didn't get that. Please tell me again.")
else:
    response = open_ai.ask_ChatGPT(query, words=100)
    sayer.say(response)
    print(response)
