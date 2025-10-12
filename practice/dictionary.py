import requests
url ="https://real-time-amazon-data.p.rapidapi.com/product-details?asin=B07ZPKBL9V&country=US"
response = requests.get(url, headers={"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com", "x-rapidapi-key": "3950f3c6d5msh4385ff32c5aa424p10ae8djsneeac0a31a6d9"})
print(response.json()["data"]["product_title"])
