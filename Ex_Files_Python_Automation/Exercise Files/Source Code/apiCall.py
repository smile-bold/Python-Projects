import requests  # doing API calls through python.
import json  # API's are a bridge between two software platforms that allows developers to create sophisticated software with minimal code.

baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "012993441012"}
response = requests.get(
    baseUrl, params=parameters
)  # first python must get the data through an API call with the required method and parameters
print(response.url)
content = response.content
info = json.loads(content)
print(type(info))
print(info)