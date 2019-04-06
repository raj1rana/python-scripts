#imports simplejson and "as" to use it as jason name
import simplejson as json
#importing os to use the file system of the operating system
import os
#if there is a file then give the status of the file
if os.path.isfile("./my.json") and os.stat("./my.json").st_size != 0:
    #read the old jason file
    oldfile = open("./my.json","r+")
    #convert the json data into python objects
    data = json.loads(oldfile.read())
    #print the data inside the file
    print("current age is ", data ["age"], "----adding a year")
    data["age"] = data["age"] +1
    print("new age is ",data["age"])
#if there is no json file in directoy then create it
else:
#open a file in cache to write (w+)
    oldfile = open("./my.json", "w+")
#filling the data inside the file
    data = {"name": "nick","age": 27}
    print("no data found setting age to ", data["age"])
#dunping the data into the file by converting the file into jason format
oldfile.seek(0)
oldfile.write(json.dumps(data))