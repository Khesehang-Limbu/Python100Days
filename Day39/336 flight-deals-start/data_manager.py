import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def getSheetyData(self):
        return requests.get(url="https://api.sheety.co/edc3c75ded3958f75612dc75cd7088b6/flight/flights").json()["flights"]

    def updateIATA(self, iataCode, id):
        update_data = {
            "sheet1": {
                "iataCode": iataCode,
            }
        }
        iata_update_response = requests.put(
            url=f"https://api.sheety.co/edc3c75ded3958f75612dc75cd7088b6/flight/sheet1/{id}",
            json=update_data)

    def getEmails(self):
        return  requests.get(url="https://api.sheety.co/edc3c75ded3958f75612dc75cd7088b6/flight/users").json()["users"]