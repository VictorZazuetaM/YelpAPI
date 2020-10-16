import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "boiOV9RrjKFrN3rBt-mmjj2GAhYM8EF3uj6YcgFYnwrtkHxMAMP1fRkhwFKYkxbNBA0QVGjlAelQwxqdXaQSV5pHyyvff5R-6ZzYqfgjPFWrNx8RW6U_cfL5CUeJX3Yx"

headers = {
    "Authorization": "Bearer " + api_key
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