#pymongo and mongo DB search is like by line inside in a document then it moves to the other document
from enum import unique

import pymongo
from pymongo import MongoClient

MyClient = MongoClient()    # again this is connecting to deault host and port

db = MyClient.mydatabase #db is a variable to store the database my database

users = db.users   #this  is the table

db.users.create_index([("names" ,pymongo.ASCENDING)])    #to create an in dex for a whole row



