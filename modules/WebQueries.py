import webbrowser


class WebQueries:
    def __init__(self) -> None:
        pass

    def open_site(self, query):
        if "open youtube" in query:
            webbrowser.open("youtube.com")
            return "opening youtube"
        elif "open google" in query:
            webbrowser.open("google.com")
            return "opening google"
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            return "opening stack overflow"
        elif "open github" in query:
            webbrowser.open("github.com")
            return "opening github"
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            return "opening facebook"
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
            return "opening instagram"
        elif "open twitter" in query:
            webbrowser.open("twitter.com")
            return "opening twitter"
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
            return "opening linkedin"
        elif "open reddit" in query:
            webbrowser.open("reddit.com")
            return "opening reddit"
        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")
            return "opening wikipedia"
        elif "open amazon" in query:
            webbrowser.open("amazon.com")
            return "opening amazon"
        elif "open flipkart" in query:
            webbrowser.open("flipkart.com")
            return "opening flipkart"
        else:
            return False
