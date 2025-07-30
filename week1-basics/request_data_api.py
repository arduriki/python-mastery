import requests

# dictionaries
query_parameters = {"language": "en"}

# Resquest from an API
response = requests.get(
    "https://uselessfacts.jsph.pl/random.json", params=query_parameters
)

# Get something specific from the json response
# Method chaining
print(response.json().get("text"))
