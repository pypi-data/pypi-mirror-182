import requests

class ChatAI:
    def __init__(self, version="last", api_key="standart_key"):
        if version=="last":
            self.v = "last"
        else:
            self.v = f"v{version}"

        self.api_key = api_key

    def get_answer(self, text):
        return requests.get(
            f"https://anapi.wsm001.repl.co/api/{self.v}",
            json={"text":text, "api_key":self.api_key}).json()["answ"]
