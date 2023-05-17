import requests
from datetime import datetime

USERNAME = "khesehang"
TOKEN = "ThisIsAToken"
GRAPH_ID = "graph1"
pixela_end_point = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create a User
# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

# Creating a Graph
headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    "id":  GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hr",
    "type": "float",
    "color": "momiji",
}
#
# response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
# print(response.text)

# POST A PIXEL
# today = datetime(year=2023, month=5, day=16)
today = datetime.now()

post_end_point = f"{graph_end_point}/{GRAPH_ID}"
post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# response = requests.post(url=post_end_point, json=post_data, headers=headers)
# print(response.text)

# Update a Pixel
update_end_point = f"{post_end_point}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": "4.5",
}

# response = requests.put(url=update_end_point, json=update_data, headers=headers)
# print(response.text)

# Delete a pixel
response = requests.delete(url=update_end_point, headers=headers)
print(response.text)