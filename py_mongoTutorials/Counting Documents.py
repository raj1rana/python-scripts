import pymongo
from pymongo import MongoClient

MyClient = MongoClient()    # again this is connecting to deault host and port

db = MyClient.mydatabase #db is a variable to store the database my database

Users = db.users   #this  is the table

"""
Users.find()
fristcount = Users.count_documents({" *": " *"})
print(fristcount)
#additional code to find additional things """

Users.find()
counted = Users.count_documents({"password": "12345"})   #this one is a replacement for count() method cause of the depriciation
print(counted)
#like here we are finding the  document Name where name is raju




