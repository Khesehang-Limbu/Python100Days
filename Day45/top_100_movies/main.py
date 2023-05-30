import requests
from bs4 import BeautifulSoup

movies_html = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(movies_html, "html.parser")

movie_list = [title.getText() for title in soup.findAll(name="h3", class_="title")]
movie_list.reverse() #alternatively, we could have used the slice operator as movie_list[::-1], slice operator syntax, list[start:stop:step]

with open("movies.txt", "w") as movie_file:
    for title in movie_list:
        movie_file.write(f"{title}\n")