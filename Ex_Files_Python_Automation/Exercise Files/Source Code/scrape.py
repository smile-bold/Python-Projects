import requests 
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'\
response = requests.get(url) #retrieves url content
soup = BeautifulSoup(response.text, 'lxml') #converts html to lxml format
quotes = soup.find_all('span', class='text') #finds only html content with span element and class of "text"
authors = soup.find_all('small', class="author")
tags = soup.find_all('div', class="tags")
for i in range(0, len(quotes));
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)