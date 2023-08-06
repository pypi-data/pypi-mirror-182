from requests import get

class Elisa():
    def __init__(self):
        self.url = 'https://chatbot.some-1hing.repl.co/chatbot'

    def elisa(self, query):
        query = "+".join(query.split(" "))
        try:
            url = f"{self.url}/{query}"
            response = get(url).json()["response"]
            return str(response)
        except:
            return "ERROR!! Elisa Chatbot not responding."
