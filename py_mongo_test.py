"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB (see Instructor comments for link to installation information)
and uncomment the get_db function.
"""
import pprint
from pymongo import MongoClient


def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert({"name" : "Egillstadir"})
    
def get_city(db):
    return db.cities.find_one({"name": "Egillstadir"})

def get_db():
    # For local use

    client = MongoClient('localhost', 27017)
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.test
    return db

if __name__ == "__main__":
    # For local use
    db = get_db() # uncomment this line if you want to run this locally
    print get_city(db)
    print get_city(db)

    print db.command("buildinfo")
    for x in db.cities.find({"name" : "Reykjavik"}):
        pprint.pprint(x)