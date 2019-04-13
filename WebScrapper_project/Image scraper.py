"""in this we will get and downlod the images from python"""
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests


#getting the inputs
search = input("tell me what do you want to search for : ")
#parameters for searching the URL
params = {"q": search}

#getting the URL
r = requests.get("http://www.bing.com/images/search", params = params)
# including the Beautifulsoup
soup  = BeautifulSoup(r.text, "html.parser")
#find images in "a" attributs  in class thumb
link = soup.findAll("a", {"class": "thumb"})
#a for loop to get the images so that the download goes continuously
for item in link:
    #a variable img_obj  to store the requests.get items links
    img_obj  = requests.get(item.attrs["href"])
    #this is to store the titles of the image and split the image name -1 is the position of the name
    title = item.attrs["href"].split("/")[-1]
    #printing the URL into the consol so that the user will know that which image is being downloaded
    print("getting : ", item.attrs["href"])
    #converting the herf into images with the help of BytsIO
    image = Image.open(BytesIO(img_obj.content))
    #saving the images into the given Directory with + title and image.format
    image.save("./downloaded_images/" + title, image.format )




#that is it this is how we save the images in python with the help of the these lib Beautifulsoup, requests, IO and Image from pillow module