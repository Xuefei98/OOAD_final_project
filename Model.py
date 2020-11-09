from pymongo import MongoClient
import dns
from User import User
from Show import Show
from Movie import Movie
###--- MVC Pattern - Model ---###

class Model:
    user = None
    showsList = None
    def __init__(self):
            cluster = MongoClient("mongodb+srv://ooaddriveinuser:ooaddriveinpassword@cluster0.b8hrp.mongodb.net/test?retryWrites=true&w=majority")
            print("Connected!")
            self.db = cluster.drivein
            self.users_collection = self.db["users"]
            self.movies_collection = self.db["movies"]
            self.theaters_collection = self.db["theaters"]
            self.food_collection = self.db["food"]
            self.shows_collection = self.db["shows"]
            self.preferences_collection = self.db["preferences"]
            
    ###--- Verifying Credentials of a User ---###
    def getCredentials(self,email): #Fetching the password for a given email id
        record = self.users_collection.find({"email":email})
        if record!=None:
            for r in record:
                return r['password']
        else:
            return None  
    def getUser(self, email):
       record = self.users_collection.find_one({"email":email})
       self.user = User(record['email'], record['genre'], record['maxDistance'], record['maxPrice'])
       return self.user 
    def getShows(self, preference):
       recordList = [] 
       moviesList = self.movies_collection.find({"genre": preference.genre})
       for movie in moviesList:
           theatersList = self.theaters_collection.find({"distance": { "$lte" : preference.maxDistance}})
           for theater in theatersList:
               showsList = self.shows_collection.find({"price":{ "$lte" : preference.maxPrice}})
               for show in showsList:
                   movieObj = Movie(movie['movieid'],movie['name'],movie['genre'],movie['duration'])
                   recordList.append(Show(movieObj, theaterObj, show['price'] ))
       return recordList
       
       
        