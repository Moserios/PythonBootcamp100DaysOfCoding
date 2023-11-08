import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

all_titles = soup.find_all(name="h3")

movies = []

for record in all_titles:
    title = record.getText()
    movies.insert(0, title)

content = ''

for record in movies:
    content += f"{record}\n"

with open ("movies.txt", "w", encoding="utf-8") as file:
    file.write(content)



#################### bootcamp solution ####################

import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
#
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3", class_="title")
#
# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
#
#
# '''
# FAQ: Empire's website has changed!
#
# When this lesson was created, I used this URL for the project:
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# However, Empire has since changed their website. You can see this when you inspect the movie title elements.
# You'll see that the h3 with the class "title" is no longer there.
# To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.
#
# '''