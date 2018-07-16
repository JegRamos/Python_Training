import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"Your request to {url} was {response.status_code}")
print(response.text)

# Getting dad jokes via text
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept" : "text/plain"})
print(f"This is the joke: {response.text}")

# Getting JSON
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {"Accept" : "application/json"})
dad_joke = response.json()
print(dad_joke["joke"])