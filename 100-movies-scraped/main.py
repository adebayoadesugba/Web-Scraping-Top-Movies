import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

# This header tells the website you are a real Chrome browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")

# Target the spans with the data-test attribute
tt = soup.find_all("span", attrs={"data-test": "content"})

# We'll store them in a list to keep them in order
movie_list = []

for item in tt:
    # Find the h2 inside the span
    title_tag = item.find("h2")
    if title_tag:
        movie_list.append(title_tag.get_text())

# Empire lists them from 100 down to 1, so let's reverse them if you want 1-100
movie_list.reverse()



# except FileNotFoundError:
with open("100-movies-scraped/movies.txt", "w", encoding="utf-8") as file:
        for movie in movie_list:
            file.write(movie + "\n")