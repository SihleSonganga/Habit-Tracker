import requests

USERNAME = "sihle"
TOKEN = "pwedyqwerty"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# graph_response = requests.post(url=graph_endpoint, json=grap_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20220720",
    "quantity": "3"
}

pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)



