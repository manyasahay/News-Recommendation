import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import re 

root = 'https://www.google.com/'
link = 'https://news.google.com/foryou?hl=en-IN&gl=IN&ceid=IN%3Aen'
#r = requests.get(url)

def news(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

# Add a delay after each request
    time.sleep(2) 
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    #print(soup)
    v = soup.find_all('div', attrs = {'class' : 'WwrzSb'})
    #print(v) 
    for item in v:
        raw_link = (item.find('a', href=True)['href'])
        print(raw_link)
        link = (raw_link.split('&url=')[1]).split('&sa=U&')[0]
        #print(item)
        title = (item.find('div', attrs = {'class':'n0jPhd ynAwRc MBeuO nDgy9'})).get_text()
        desc = (item.find('div', attrs = {'class':'GI74Re nDgy9d'})).get_text()
        title = title.replace(",", "")
        desc = desc.replace(",", "")
        desc_withouttime = re.split(r'\.{2}', desc)
        print(title)
        print(desc_withouttime)
        # print(link_split)
        document = open("data.csv", "a", encoding = "utf-8")
        document.write("{},{},{} \n".format(title,desc_withouttime,link))
        document.close()
    p = soup.find_all('p')
    print(p)
    next = soup.find('a', attrs = {'aria-label':'Next page'})
    if next:
        next = (next['href'])
        link = root + next
    news(link)
news(link)