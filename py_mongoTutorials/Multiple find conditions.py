import pymongo
from pymongo import MongoClient

MyClient = MongoClient()    # again this is connecting to deault host and port

db = MyClient.mydatabase #db is a variable to store the database my database

Users = db.users   #this  is the table



#like here we are finding the  document Name where name is raju



lastcount = Users.count_documents({"password": "gadha","Name": "biju"})
print(lastcount)
