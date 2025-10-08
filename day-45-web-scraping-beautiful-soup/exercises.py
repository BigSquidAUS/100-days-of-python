from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(class_="titleline")
article_scores = soup.find_all(name="span", class_="score")

article_texts = []
article_links = []
article_votes = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.find("a").get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

for votes in article_scores:
    article_votes.append(int(votes.get_text().split()[0]))

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)
print(f"Most popular article: {article_texts[largest_index]}: {article_links[largest_index]} ({article_votes[largest_index]} votes)")

# with open("website.html","r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup.title)
# #print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)