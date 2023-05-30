from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

yc_soup = BeautifulSoup(yc_webpage, "html.parser")
titles = [title.getText() for title in yc_soup.select(selector=".titleline:nth-child(1)")]
links = [title.a.get("href") for title in yc_soup.select(selector=".titleline:nth-child(1)")]
points = [int(point.getText().split()[0]) for point in yc_soup.select(selector=".score")]
max_points = max(points)
index_of_max_points = points.index(max_points)

print(titles[index_of_max_points])
print(links[index_of_max_points])
print(points[index_of_max_points])

# for title in titles:
#     print(title.getText())
#     print(title.a.get("href"))
#
# for point in points:
#     print(point.getText())
# with open(file="website.html") as website_file:
#     contents = website_file.read()
#     soup = BeautifulSoup(contents, "html.parser")

