from bs4 import BeautifulSoup
import requests

# Project1
# url = "https://webscraper.io/test-sites/tables"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')
# # print(soup)

# headings1 = soup.find_all('h1')
# headings2 = soup.find_all('h2')
# image= soup.find_all('img')

# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]

# last_names = []

# for row in rows:
#     last_names.append(row.find_all('td')[2].get_text())

# print(last_names)

#Project2
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data_types = soup.find(class_='wikitable')
body = data_types.find('tbody')
rows = body.find_all('tr')[1:]

mutable_types = []
immutable_types = []

for row in rows:
    data = row.find_all('td')
    if data[1].get_text() == 'mutable\n':
        mutable_types.append(data[0].get_text().strip())
    else:
        immutable_types.append(data[0].get_text().strip())
    
print(f"Mutable Types: {mutable_types}")
print(f"IMMutable Types: {immutable_types}")
