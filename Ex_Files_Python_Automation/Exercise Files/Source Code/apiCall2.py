import requests

baseurl = "http://api.openweathermap.org/data/2.5/forecast"  # baseurl
parameters = {
    "APPID": "6918961fcc16aa6582543233b2060914",
    "q": "Newland",
}  # set parameters to receive from API
response = requests.get(baseurl, params=parameters)  # store response
print(response.content)  # show's api 3 hour forecast
# RAPIDAPI.com free marketplace of API; allows the capability to create a software development kit using multiple chain APIS
# check beautifulsoup, selenium, and the requests documentation libraries.
