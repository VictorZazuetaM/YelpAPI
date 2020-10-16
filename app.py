import requests
import config

url = "https://api.yelp.com/v3/businesses/search"


headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Restaurants",
    "location": "Culiacan"
}

response = requests.get(url, headers=headers, params=params)
restaurants = response.json()["businesses"]
restaurant_names = [restaurant["name"] for restaurant in restaurants]
for restaurant in restaurant_names:
    print(restaurant)