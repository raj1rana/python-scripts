import requests
from io import BytesIO
from PIL import Image

#to get the image URL
r = requests.get("https://cdn2.unrealengine.com/Unreal+Engine%2Fblog%2Fepic-announces-unreal-engine-marketplace-88-12-revenue-share%2FFEATURE_UEMarketplace_RevenuShare-1920x960-0b8bb62bee720e2f5c3e4fca10e6d31e080f9266.jpg")

#is to print the status if the URL when we will request it
print("status code :", r.status_code)

#creating the image from the binary data that we received from the URL
#also we are converting the binary data and storing the information into image variable
image = Image.open(BytesIO(r.content))  #r. content will open the file with its content it is not like r.text which wil only return text
#path to save image
path = "./image." + image.format
#a try statement to save the image
try:
    image.save(path)
#this part is to display the error
except IOError:
    print("cnnot save the image")

