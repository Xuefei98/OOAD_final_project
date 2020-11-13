from pymongo import MongoClient
import dns
from User import User
from Show import Show
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
        record = self.users_collection.find_one({"email":email})
        if record!=None:
            print(record['password'])
            return record['password']
        else:
            return None  
    def getUser(self, email):
       record = self.users_collection.find_one({"email":email})
       self.user = User(record['email'], record['genre'], record['maxDistance'], record['maxPrice'])
       return self.user 
    def addUser(self,record):
        email = record['email']
        password = record['password']
        genre = record['genre']
        maxDistance = record['maxDistance']
        maxPrice = record['maxPrice']
        doc = {"email": email, "password": password, "genre": genre, "maxDistance": int(maxDistance), "maxPrice": int(maxPrice)}
        self.users_collection.insert_one(doc)      
    def getShows(self, preference):
       recordList = [] 
       showsList = self.shows_collection.find({"price":{ "$lte" : preference['maxPrice']}})
       print("shows")
       for show in showsList:
           theatersList = self.theaters_collection.find({"theaterid": show['theaterid'], "distance": { "$lte" : preference['maxDistance']}})
           for theater in theatersList:
               moviesList = self.movies_collection.find({"movieid": show['movieid'], "genre": preference['genre']})
               for movie in moviesList:
                   d = dict()
                   d['movieName'] = movie['name']
                   d['duration'] = movie['duration']
                   d['genre'] = movie['genre']
                   d['movieid'] = movie['movieid']
                   d['theaterName'] = theater['name']
                   d['distance'] = theater['distance']
                   d['theaterid'] = theater['theaterid']
                   d['showid'] = show['showid']
                   d['price'] = show['price']
                   d['foodList'] = []
                   for item in theater['foodList']:
                       fooditem = self.food_collection.find_one({"foodid": item})
                       e = dict()
                       e['foodName'] = fooditem['name']
                       e['foodid'] = fooditem['foodid']
                       e['foodprice'] = fooditem['price']  
                       d['foodList'].append(e)    
                   recordList.append(Show(d))
       return recordList
   
    def updatePreferences(self, email, genre, maxDistance, maxPrice):
        self.users_collection.update({"email":email}, { "$set": {"genre": genre, "maxDistance": int(maxDistance), "maxPrice": int(maxPrice)}})
        return self.getUser(email)
       
        