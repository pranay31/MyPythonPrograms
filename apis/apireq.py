import requests
response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=middlesex" )

print response.status_code
print response.content
print type(response.content)
print response.json()

print type(response.json())

# Get the content-type from the dictionary.

"""response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print response.status_code"""
# 9 people are currently in space.
#print(data["number"])
#print(data)
