# Create a .txt file with the top 100 movies, starting from number 1, based on the Empire website.
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup =  BeautifulSoup(response.text,"html.parser")

movies_soup = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in movies_soup]

movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")