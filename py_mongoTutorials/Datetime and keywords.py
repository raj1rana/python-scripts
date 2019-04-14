#datetime is used to record the date into the DB as well as into the application
import datetime
import pymongo
from pymongo import MongoClient

MyClient = MongoClient()    # again this is connecting to deault host and port

db = MyClient.mydatabase #db is a variable to store the database my database

users = db.users   #this  is the table
date = datetime.datetime.now()
#print(date)

old_date = datetime.datetime(2015, 11 , 30 )

users.insert_one({"UID": "1", "date": date})



old_datecount = users.find({"date": {"$gt": old_date}})      #HERE $gte is greater then equal to or gt means greater then
old = users.count_documents({"date": {"$gt": old_date}})
print(old)


query = users.count_documents({"date":{"$exists": True}})    #  here we are looking into the $exists permieter looking for the date
print(query)

#NOTE : we can also use $ne for not equal to and $e for equal to in the count function