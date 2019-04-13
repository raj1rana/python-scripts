from bs4 import BeautifulSoup  #importing the Beautiful soup
import requests #importing requests

search = input("enter what you want to search: ") #this is user input

params = {"q": search} #parameters to search
r = requests.get("http://bing.com/search", params=params) #this is used to send thee request

soup = BeautifulSoup(r.text, "html.parser") #this is to beautify the r.text inpiuts
print(soup.prettify())


# this is for making a file fro r.text input
w = open("./main.html", "w+")

w.write(r.text)
