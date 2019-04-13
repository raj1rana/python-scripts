'''this is for getting a proper webpage from beautigul soup as well as here we
are looking for only likns and text in our previous example we got the whole page
herer the results and links variable are responsible to to get the order list and links
from the webpage

here the for statement and if statement is responsible to get the URLS and text form the webpage
'''
from bs4 import BeautifulSoup
import requests

search = input("what do you want to searh for: ")
params = {"q": search}

r = requests.get("http://www.bing.com/search", params = params)

soup=  BeautifulSoup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})

links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)