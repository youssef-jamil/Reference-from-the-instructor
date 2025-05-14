import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")
#most of the time, the books are in the article tag
for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    print("Book titled: " + title + " has a rating of: " + rating + " stars")
