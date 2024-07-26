import requests
from bs4 import BeautifulSoup

url = input("Input the URL:\n> ")
#control for the site in nature.com and articles 
if not "www.nature.com" in url or not "articles" in url.split("/"):
    print("\nInvalid page!")
    exit()

response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find('title')
meta = soup.find('meta', {'name': 'description'})

d = {title: title.text, meta: meta['content']}

print(d)
