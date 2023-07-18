import webbrowser


class WebQueries:
    def __init__(self) -> None:
        pass

    def open_site(self, query):
        if "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open github" in query:
            webbrowser.open("github.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "open twitter" in query:
            webbrowser.open("twitter.com")
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
        elif "open reddit" in query:
            webbrowser.open("reddit.com")
        elif "open wikipedia":
            webbrowser.open("wikipedia.com")
        elif "open amazon" in query:
            webbrowser.open("amazon.com")
        elif "open flipkart" in query:
            webbrowser.open("flipkart.com")
        else:
            pass
