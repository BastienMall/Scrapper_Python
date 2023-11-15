import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):

    quote_elements = soup.find_all('div', class_='paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2')

    for quote_element in quote_elements:

        title = quote_element.find('p', class_='typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2').text

        scoring = quote_element.find('p', class_='typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7').text

        domaine = quote_element.find('span', class_='typography_body-s__aY15Q typography_appearance-default__AAY17').text


        quotes.append(
            {
                'Entreprise': title,
                'Notation': scoring,
                'Domaine': domaine
            }
        )

url = 'https://fr.trustpilot.com/categories/contractors_consultants'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = []

scrape_page(soup, quotes)

next_li_element = soup.find('li', class_='next')

while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    page = requests.get(url + next_page_relative_url)

    soup = BeautifulSoup(page.text, 'html.parser')

    scrape_page(soup, quotes)

    next_li_element = soup.find('li', class_='next')

csv_file = open('Scoring.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(csv_file)

writer.writerow(['Entreprise', 'Notation', 'Domaine'])

for quote in quotes:
    writer.writerow(quote.values())

csv_file.close()