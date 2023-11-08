from bs4 import BeautifulSoup
import lxml
import requests

############################# ONLINE

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")#"html.parser") #lxml

# result_container = soup.find_all('div', {'class':'clearfix'})
# url_part_1 = 'https://www.entega.de/sitemap/'
# url_part_2 = []
# for item in result_container:
#     for link in item.find_all ('a', {'class':'modSitemap__lvl1Link ui-link' }):
#         url_part_2.append (link.get ('href'))

all = soup.find_all(class_="subline")
# print(all)

all_a = soup.find_all(class_="athing")
# all_a = soup.find_all("span", {"class":"athing"}, "a")
# all_a = soup.find_all("span", {"class":"titleline"}, "a")
# print(all_a)
# soup.find(name="h1", id="name")
# counter = 1
# print(all_a)
titles = []
links = []
votes = []
# counter = 1
for tag in all_a:
    print(tag.prettify())
    id = tag.get("id")
    id_score = str(f"score_{id}")
    try:
        vote = int(soup.find(id=id_score).getText().split()[0])
        # print(f"{counter}.{vote}")
    except:
        vote = 0
        # print(f"{counter}.{vote}")
    votes.append(vote)

    title = tag.find("span", class_="titleline").find("a").getText()# .find("span", class_="titleline").find("a")
    titles.append(title)

    link = tag.find("span", class_="titleline").find("a").get("href")
    links.append(link)
    # print(link)
    # counter += 1

print(titles)
print(links)
print(votes)


max_index = votes.index(max(votes))
print(max_index)
print(titles[max_index])
print(links[max_index])
print(votes[max_index])


############### LOCAL
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.a) #prints first <a> tag
# print(soup.p) #prints first <p> tag
# print(soup.li) #prints first <li> tag
#
# # if you want to print all tags of particular type:
# all_tags_a = soup.findAll(name="a")
# print(all_tags_a)
# all_tags_p = soup.findAll(name="p")
#
# for tag in all_tags_a:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.getText())
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# name = soup.select("#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)

