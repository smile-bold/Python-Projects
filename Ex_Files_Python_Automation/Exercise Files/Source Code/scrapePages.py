from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1
response = requests.get(url) #grab url data
soup = BeautifulSoup(response.text, 'lxml') #parse into lxml
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4') #stores outer layer of data in variable
for i in items: #loop through data store titles and price for each product. 
    itemName = i.find('h4', class_='card-title').text.strip('\n') # function expression that removes character or something from data
    itemPrice = i.find('h5').text
    print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pagination = soup.find('ul', class_='pagination') #finds unordered list with class of "pagination"
pages = pagination.find_all('a', class_='page-link') #finds all links with class "page-link"
urls = []
for page in pages:
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        link = page.get('href') #retrieves hyperlink reference
        urls.append(link) #Adds page number onto url element in array
for i in urls:
    response = requests.get(url + i) # Adds already retrieved url content into a new scrape of url content then loops through it
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1