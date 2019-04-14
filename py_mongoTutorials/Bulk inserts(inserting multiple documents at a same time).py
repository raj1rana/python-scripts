"""in this example we are going to create a DB also with a table and insert a row into it lets see how it goes """
import pymongo    # impporting the py mongo
from pymongo import MongoClient      #importing mongo_client from py mongo

MyClient = MongoClient()    # creating a client variable and MongoClient() is a function

#this is to define or call a DB name
db = MyClient.mydatabase  # you can also write this as MyClient["my_database"] only if there is a _ in the database name
#this is a creation of a table called users
Users = db.users # again if there is a _ then we can use a [] for accessing the table
#these are the table perimeters  along woith lists in the end
users = [{"Name ": "raju", "password": "12345"}, {"Name": "biju", "password": "gadha"}]   #these are multiple arguments that we need to add inside the Database
#this is to insert the documents into the db
ins = Users.insert_many(users)

