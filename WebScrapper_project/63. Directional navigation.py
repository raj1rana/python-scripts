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
        print("summery  : ", item.find("a").parent.parent.find("p").text) #for printing the summery for the page  and parent class in html directive


        children = item.children

        for child in children:
            print("child :" ,child)