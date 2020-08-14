from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'http://books.toscrape.com/'
url


#getting HTML
page = requests.get(url)


page_html = BeautifulSoup(page.text, 'html.parser')
#print(page_html.prettify())


#finding h1 tag
page_html.find('h1').text
#also the same as
#page_html.h1.text


page_html.find_all('article')


page_html.find('article').find("a")


page_html.find('article').find("a")['href']


#li(class = next) a href "catalouge"
page_html.find_all('li',{"class":"next"})


page_html.find('li',{"class":"next"}).a['href']


#use this instead
page_html.find('li',class_="next").a['href']


base_url = "http://books.toscrape.com/"


def get_title_links_and_next_page(page_url):
    #this is where we store our links to the title 
    list_links = [] 
    #get the html for the url that was given
    page = requests.get(base_url)
    #parse the html file for beautifulsoup to query on
    soup = BeautifulSoup(page.text, 'html.parser')
    #inspecting the page we notice that the books are placed under 
    #the article tag so we get all articles
    for article in soup.find_all('article'):
        #the article tag has an anchor tag so we find it and get the href
        if "catalogue" not in article.find("a")['href']:
            url = base_url + "catalogue/" + article.find("a")['href']
        else:
            url = base_url + article.find("a")['href']
        #add the title url to our list of titles 
        list_links.append(url)
    
    #try to check if a next button is in the page 
    try:
        next_url = page_html.find('li',{"class":"next"}).a['href']
    #if none we return None :)     
    except:
        next_url = None

    return (list_links, next_url)


res = get_title_links_and_next_page('http://books.toscrape.com/index.html')
title_links = res[0]
title_links


while res[1]:
    #print("blah")
    if "catalogue" not in res[1]:
        page_url = base_url + "catalogue/" + res[1]
    else:
        page_url = base_url + res[1]   
    res = get_title_links_and_next_page(page_url)
    title_links += res[0]

title_links


res


# get title
page_html.find('h3').a['title']


#get price
page_html.find('p',class_="price_color").text


url_blah = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
soup_page = requests.get(url_blah)
soup_html = BeautifulSoup(soup_page.text, 'html.parser')


#title
print(soup_html.h1.text.strip())
print() #price
print(soup_html.find('p',class_="price_color").text)
#price print(soup_html.find('p').text)

#desc
print()
print(soup_html.find_all('p')[-1].text)

#stock
print()
print(soup_html.find('p',class_="instock availability").text.strip())


print(soup_html.find_all('p')[-1].text)
print(soup_html.find('p',class_="instock availability").text.strip())


#availability
#print(soup_html.find('p',class_="instock availability").text.strip())
print(soup_html.i.next_sibling)
print(soup_html.find('p',class_="instock availability").text.strip())


print(soup_html.prettify())


def get_title(soup):
    soup.h1.text.strip()
    return 

def get_price(soup):
    soup.find('p',class_="price_color").text
    return 
    
def get_description(soup):
    soup.find_all('p')[-1].text
    return 
    
def get_availability(soup):
    soup.find('p',class_="instock availability").text.strip()
    return 

book_data = []
for title_link in title_links: 
    page = requests.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    title = get_title(soup)
    price = get_price(soup)
    description = get_description(soup)
    availability = get_availability(soup)
    
    book_data += [[title, price, description, availability]]



