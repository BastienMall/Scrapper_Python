import requests
from bs4 import BeautifulSoup as bs

url="https://quotes.toscrape.com/"
page = requests.get(url)

html = page.content

soup = bs(page.text, 'html.parser')

# text_elements = soup.text.get_text()
authors_elements = soup.find_all(class_='author')

print(soup.span.get_text())
print(authors_elements)


titre_articles = soup.find_all(class_='text')
for titre in titre_articles:
    print(titre.get_text(strip=True))

authors_articles = soup.find_all(class_='author')
for author in authors_articles:
    print(author.get_text(strip=True))