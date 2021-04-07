import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACfa28bd73d6b6a0c84cccca3dc4d1116b"
auth_token = "..."

weather_params = {
    "lat": 52.520008,
    "lon": 13.404954,
    "appid": "...",
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# !! LIST SLICING: !!
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="twillio.com generated number",
        to="My verified phone number"
    )
print(message.status)
# own approach
# id_list = []
# for num in range(0, 11):
#     condition_code = weather_data["hourly"][num]["weather"][0]["id"]
#     id_list.append(condition_code)
#     if int(condition_code) < 700:
#         print("Bring an Umbrella")
