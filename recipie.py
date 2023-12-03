import requests

url = "https://the-recipes.p.rapidapi.com/recipes/allrecipes"

headers = {
	"X-RapidAPI-Key": "cacaac5b8fmsh4ba079d838f6e8bp1e632ajsnd8748447633a",
	"X-RapidAPI-Host": "the-recipes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())