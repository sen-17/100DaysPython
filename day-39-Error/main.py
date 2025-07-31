# ========================= API ERROR ===============================================


# import requests

# API_KEY = "TAVHysARuZYppBh14bSFgMhxLTjI0CFI"
# API_SECRET = "XUgQIrFTXbcsY9ip"
# ACCESS_TOKEN = "gALNJpnHA9deoi9lCeQNxuqpb9jk"

# # URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

# # data = {
# #     "grant_type": "client_credentials",
# #     "client_id": API_KEY,
# #     "client_secret": API_SECRET
# # }

# # headers = {
# #     "Content-Type": "application/x-www-form-urlencoded"
# # }

# # response = requests.post(URL, data=data, headers=headers)
# # print(response.text)

# BASE_URL ="https://test.api.amadeus.com/v2/shopping/flight-offers"
# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}"
# }

# params = {
#     "originLocationCode": "MAD",
#     "destinationLocationCode": "CDG",
#     "departureDate": "2025-07-24",
#     "adults" : 1
# }

# response = requests.get(BASE_URL, params=params, headers=headers)
# print(response.text)