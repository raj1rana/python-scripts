"""in this we will get and downlod the images from python here we create a functuon and call it two times that turn this into a loop"""
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import  os           #importing the os LIB for creating the dir


def strt_search():
    #getting the inputs
    search = input("tell me what do you want to search for : ")
    #parameters for searching the URL
    params = {"q": search}

    #thi dir function will take the dir name value from search variable as search.replace is written here
    dir_name = search.replace(" ", "_").lower()    #variable dir_name should  replace all spaces with _ and name should be in lowercase
    if not os.path(dir_name):   # if the direcroty is not present then
        os.makedirs(dir_name)   #create the directory same as value stored in variable dir_name
    #getting the URL
    r = requests.get("http://www.bing.com/images/search", params = params)
    # including the Beautifulsoup
    soup  = BeautifulSoup(r.text, "html.parser")
    #find images in "a" attributs  in class thumb
    link = soup.findAll("a", {"class": "thumb"})
    #a for loop to get the images so that the download goes continuously
    for item in link:
        try:
            #a variable img_obj  to store the requests.get items links
            img_obj  = requests.get(item.attrs["href"])
            #this is to store the titles of the image and split the image name -1 is the position of the name
            title = item.attrs["href"].split("/")[-1]
            #printing the URL into the consol so that the user will know that which image is being downloaded
            try:
                print("getting : ", item.attrs["href"])
                #converting the herf into images with the help of BytsIO
                image = Image.open(BytesIO(img_obj.content))
                #saving the images into the given Directory with + title and image.format
                image.save("./"+ dir_name +"/" title, image.format )

            except:
                print("could not save image")
        except:
            print("could not save the image")
    strt_search()
strt_search()

