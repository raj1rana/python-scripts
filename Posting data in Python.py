import requests
my_data = {"name": "raj", "email": "raj1rana"}
r = requests.get("https://www.w3schools.com/php/welcome.php", data= my_data )
f =open("./myFile.html","w+")
f.write(r.text)