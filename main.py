import requests
import datetime as dt

USERNAME  = "raghav001"
TOKEN = "abshjfkdslld34"
GRAPH_ID = "graph001"

pixela_endpoint = "https://pixe.la/v1/users"

today = dt.datetime.now()
FORMATTED_DATE = today.strftime("%Y%m%d")


#POST GRAPH:
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url = pixela_endpoint,json=user_params)
# print(response.text)



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Reading",
    "unit":"Pages",
    "type":"int",
    "color":"sora"
}

headers  = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url  = graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#POST TRACKING ACTS
pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date":FORMATTED_DATE,
    "quantity":input("Enter the number of pages you read Today?? "),

}

response = requests.post(url = pixel_add_endpoint,json=pixel_config,headers=headers)
print(response.text)

#UPDATE THE DATA WITH PUT:
# put_endpoint = f"{pixel_add_endpoint}/{FORMATTED_DATE}"

# put_config = {
#     "quantity":"13",
# }

# response = requests.put(url = put_endpoint,json=put_config,headers=headers)
# print(response.text)

