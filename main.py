import requests
from datetime import datetime

# ---------------------------- CONSTANT VARIABLES ------------------------------- #
USERNAME = "saltal27"
TOKEN = "jasfhdhfioa38402y58id89y0d81ih2di890ed"
HEADERS = {"X-USER-TOKEN": TOKEN}
GRAPH_ID = "pythontest"

# ---------------------------- CREATING USER ACCOUNT ------------------------------- #
# user_api_endpoint = "https://pixe.la/v1/users"
# user_request_body = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# user_account_response = requests.post(url=user_api_endpoint, json=user_request_body)

# ---------------------------- CREATING A NEW GRAPH ------------------------------- #
# graph_api_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
# graph_request_body = {
#     "id": "pythontest",
#     "name": "Python Test",
#     "unit": "minute",
#     "type": "int",
#     "color": "momiji",
# }

# graph_response = requests.post(url=graph_api_endpoint, json=graph_request_body, headers=HEADERS)

# ---------------------------- CREATING / UPDATING A PIXEL ------------------------------- #
today = datetime.now()

pixel_api_endpoint = f"https://pixe.la/v1/users/{USERNAME}/{GRAPH_ID}/pythontest"
pixel_request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9",
}

# pixel_response = requests.post(url=pixel_api_endpoint, json=pixel_request_body, headers=HEADERS)

# ---------------------------- DELETING A PIXEL ------------------------------- #
delete_pixel_api_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_pixel_response = requests.delete(url=delete_pixel_api_endpoint, headers=HEADERS)
