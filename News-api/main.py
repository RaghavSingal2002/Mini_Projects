import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    print("Error: NEWS_API_KEY not found in environment variables")
    exit()

query = input("What type of news are you interested in today? ")

url = "https://newsapi.org/v2/everything"

params = {
    "q": query,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": api_key
}

response = requests.get(url, params=params)
data = response.json()

if data.get("status") != "ok":
    print("API Error:", data.get("message"))
else:
    articles = data.get("articles", [])
    if not articles:
        print("No news found.")
    for index, article in enumerate(articles, start=1):
        print(index, article.get("title"))
        print(article.get("url"))
        print("\n" + "*" * 40 + "\n")
