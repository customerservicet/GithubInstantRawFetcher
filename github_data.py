import requests
import json

class GithubData:
    data = ""
    set_data = True

    def __init__(self, init_data):
        set_data = init_data

    def fetch(self, url):
        response = requests.get(url)
        data = response.text.replace("\n", "")
        if self.set_data == True:
            self.data = data
        return data
    
    def turn_to_value(self, data):
        json_data = json.loads(data)
        raw_lines = json_data["payload"]["blob"]["rawLines"]
        data = ""
        for raw_line in raw_lines:
            data += raw_line + "\n"
        if self.set_data == True:
            self.data = data
        return data