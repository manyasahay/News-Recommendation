import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import nltk
from newspaper import Article
import csv

def get_article_info(url):
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    return article.title, article.summary, article.publish_date

driver = webdriver.Chrome()
root = 'https://www.google.com/'
link = 'https://news.google.com/search?q=political&hl=en-IN&gl=IN&ceid=IN%3Aen'

driver.get(link)
driver.implicitly_wait(10)  # Wait for the page to load

# Find elements by class name
parent_elements = driver.find_elements(By.CLASS_NAME, 'm5k28')

with open('articles.csv', mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Summary', 'Date', 'Link'])
    
    for parent_element in parent_elements:
        link_element = parent_element.find_element(By.TAG_NAME, 'a')
        href = link_element.get_attribute('href')
        text = parent_element.text
        
        title, summary, date = get_article_info(href)
        
        print("Title:", title)
        print("Summary:", summary)
        print("Date:", date)
        print("Link:", href)
        
        writer.writerow([title, summary, date, href])

driver.quit()

