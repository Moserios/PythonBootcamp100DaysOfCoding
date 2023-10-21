import requests
import datetime


## Create a USER
USERNAME = "moserios"
TOKEN = "1ET2D423T4YG5n7v8c9b7czxb6d"
GRAPHID = "coding-python"

pixela_url = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = reg_response = requests.post(url=pixela_url,json=user_params)
# print(response.text)

############# Create a board ##############

graph_url = f"{pixela_url}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPHID,
    "name": "Studying Python",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
#
# graph_response = requests.post(url=graph_url, json=graph_config, headers=headers)
# print(graph_response)


############## Fill NEW pixel at the board ##########

date_now = datetime.datetime.now().strftime("%Y%m%d")
# print(date_now)

fill_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}"

fill_config = {
    "date": date_now,
    "quantity": "4.0",
}

# fill_response = requests.post(url=fill_url, json=fill_config, headers=headers)
# print(fill_response.text)

############## Update existing pixel at the board ##########
update_date = datetime.datetime(year=2023, month=10, day=1).strftime("%Y%m%d")
update_value = 10
# print(update_date.strftime("%Y%m%d"))


update_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}/{update_date}"

update_config = {
    "quantity": str(update_value)
}
# #
# put_response = requests.put(url=update_url, json=update_config, headers=headers)
# print(put_response.text)


################# Delete existing pixel ##############
delete_date = datetime.datetime(year=2023, month=10, day=1).strftime("%Y%m%d")

delete_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}/{delete_date}"

delete_response = requests.delete(url=delete_url, headers=headers)
print(delete_response.text)
