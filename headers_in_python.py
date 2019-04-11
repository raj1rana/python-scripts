import requests #importing requests
import simplejson as json   #importing simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"     #our Request URL
payload = {"longURL": "http://exapmle.com"}  #Payload URL this URL we are sending to url variable
headers = {"Content-Type":"application/json"}# this is a json header application/json
r = requests.post(url,json=payload,headers=headers) #here we post the url and tells the json that payload is the data and headers that json wil use will be headers variables

print(r.headers) #This is to print the Headers that being send back from the sever

w  = open("./PostingHeaders.json","w+")  #here we create a new file and open it with write permission

write = (r.text)   # herer we assing the write variable is equal to r.text variable

w.write(write)  # here we write the variables

