#importing request module
import requests
#searching for a parameter pizza in bing.com
params = {"q": "pizza"}
#r is  a varible that will store the request of the URL
r = requests.get("https://www.bing.com/search", params= params) #first params is a parimeter and the other one is params variable
#printing the r variable as text
print(r.text)
#opeaning a file pulledwebpage.html with write permisson
f = open("./pulledwebpage.html", "w+")
#writing the data inside the r variable inside the nwely created file
f.write(r.text)


