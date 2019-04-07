#importing request module
import requests
#r is  a varible that will store the request of the URL
r = requests.get("https://google.com")
#printing the r variable as text
print(r.text)
#opeaning a file pulledwebpage.html with write permisson
f = open("./pulledwebpage.html", "w+")
#writing the data inside the r variable inside the nwely created file
f.write(r.text)


