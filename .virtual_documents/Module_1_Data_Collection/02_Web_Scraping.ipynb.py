from bs4 import BeautifulSoup
import requests
import pandas as pd


#get the html from one of the books in the website
page = requests.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

#feed it into beautiful soup for parsing
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())


# #the find function returns the tag of the element if we want to remove the tags we call the .text attribute 
print(soup.find('h1'))
print(soup.find('h1').text)


print(soup.find('p', attrs={'class':'price_color'}))
print(soup.find('p', attrs={'class':'price_color'}).text)


p_results = soup.find_all('p')
p_results


p_results[-1].text


print(soup.find('p', attrs={'class':'price_color'}).next_sibling.next_sibling)


table_res = soup.find('table', class_="table-striped")
print(table_res.prettify())


for row in table_res.find_all('tr'):
    header = row.find('th').text
    data = row.find('td').text
    print(f"{header}={data}")
