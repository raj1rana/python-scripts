"""in this example we are going to create a DB also with a table and insert a row into it lets see how it goes """
import pymongo    # impporting the py mongo
from pymongo import MongoClient      #importing mongo_client from py mongo

MyClient = MongoClient()    # creating a client variable and MongoClient() is a function

#this is to define or call a DB name
db = MyClient.mydatabase  # you can also write this as MyClient["my_database"] only if there is a _ in the database name
#this is a creation of a table called users
users = db.users # again if there is a _ then we can use a [] for accessing the table
#these are the table perimeters  along woith lists in the end
user1 = {"name": "robot", "password": "iwillnottellyou", "position": "server_god", "hobbies":["pythom","football","boxing","tv"]}
#this is to insert the User1 column along with a ID for the record
user_id = users.insert_one(user1).inserted_id


# now let us see the output of the code