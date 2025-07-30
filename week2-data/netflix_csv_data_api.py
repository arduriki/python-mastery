import requests

# through an API
response = requests.get(
    "https://raw.githubusercontent.com/arduriki/python-mastery/refs/heads/main/week2/netflix_titles.csv"
)

data = response.text.split("\r\n")

print(data)

for row in data:
    for element in row.split(","):
        print(element)
