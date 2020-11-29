from pymongo import MongoClient
import dns
###--- MVC Pattern - Model ---###

class Model:
    def __init__(self):
            cluster = MongoClient("mongodb+srv://ooaddriveinuser:ooaddriveinpassword@cluster0.b8hrp.mongodb.net/test?retryWrites=true&w=majority")
            print("Connected!")
            self.db = cluster.drivein
            self.movies_collection = self.db["movies"]
            self.theaters_collection = self.db["theaters"]
            self.food_collection = self.db["food"]
            self.shows_collection = self.db["shows"]
            self.users_collection = self.db["users"]
    ###--- Adding New Movies to the Database ---###
    def add_Movies(self,record):
        movieid = record['movieid']
        name = record['name']
        duration = record['duration']
        genre = record['genre']
        doc = {"movieid": movieid, "name": name, "duration": duration, "genre": genre}
        self.movies_collection.insert_one(doc)   
   ###--- Adding New Theaters to the Database ---###
    def add_Theaters(self,record):
        theaterid = record['theaterid']
        name = record['name']
        distance = record['distance']
        isFoodAvailable = record['isFoodAvailable']
        foodList = record['foodList']
        doc = {"theaterid": theaterid, "name": name, "distance": distance, "isFoodAvailable": isFoodAvailable, "foodList": foodList}
        self.theaters_collection.insert_one(doc)   
   ###--- Adding New Food in theaters to the Database ---###
    def add_Food(self,record):
        foodid = record['foodid']
        name = record['name']
        price = record['price']
        availableQuantity = record['availableQuantity']
        doc = {"foodid": foodid, "name": name, "price": price, "availableQuantity": availableQuantity}
        self.food_collection.insert_one(doc)  
   ###--- Adding New Shows to the Database ---###
    def add_Shows(self,record):
        showid = record['showid']
        theaterid = record['theaterid']
        movieid = record['movieid']
        price = record['price']
        availableSlots = record['availableSlots']
        doc = {"showid": showid, "theaterid": theaterid, "movieid": movieid, "price": price, "availableSlots": availableSlots}
        self.shows_collection.insert_one(doc)       
   ###--- Adding New Users to the Database ---###
    def add_User(self,record):
        email = record['email']
        password = record['password']
        genre = record['genre']
        maxDistance = record['maxDistance']
        maxPrice = record['maxPrice']
        doc = {"email": email, "password": password, "genre": genre, "maxDistance": maxDistance, "maxPrice": maxPrice}
        self.users_collection.insert_one(doc)      
                
m1 = Model() 
"""
m1.add_Movies({"movieid": 1, "name": "Tenet", "duration": 140, "genre": "Action"})   
m1.add_Movies({"movieid": 2, "name": "Let him Go", "duration": 113, "genre": "Drama"})
m1.add_Movies({"movieid": 3, "name": "Mortal", "duration": 104, "genre": "Action"})       
m1.add_Movies({"movieid": 4, "name": "Ammonite", "duration": 120, "genre": "Romance"}) 

m1.add_Theaters({"theaterid": 1, "name": "The 88 Drive in Theater", "distance": 1.5, "isFoodAvailable": True, "foodList": [1,2]})   
m1.add_Theaters({"theaterid": 2, "name": "Boulder mart Drive in", "distance": 0.5, "isFoodAvailable": True, "foodList": [3,4]}) 
m1.add_Theaters({"theaterid": 3, "name": "Sonic Drive in", "distance": 2.5, "isFoodAvailable": True, "foodList": [5,6]}) 

m1.add_Food({"foodid": 1, "name": "Popcorn", "price": 15, "availableQuantity": 10})   
m1.add_Food({"foodid": 2, "name": "Beer", "price": 20, "availableQuantity": 10})  
m1.add_Food({"foodid": 3, "name": "Popcorn", "price": 15, "availableQuantity": 10})   
m1.add_Food({"foodid": 4, "name": "Beer", "price": 20, "availableQuantity": 10})   
m1.add_Food({"foodid": 5, "name": "Popcorn", "price": 15, "availableQuantity": 10})   
m1.add_Food({"foodid": 6, "name": "Beer", "price": 20, "availableQuantity": 10})   


m1.add_Shows({"showid": 1, "theaterid": 1, "movieid": 1, "price": 20, "availableSlots": 30 })  
m1.add_Shows({"showid": 2, "theaterid": 2, "movieid": 3, "price": 15, "availableSlots": 30 }) 
 
m1.add_User({"email": "john@gmail.com", "password": "password", "genre": "Action", "maxDistance": 2, "maxPrice": 30})
"""
showid=62
for movieid in range(0,9):
    movieid=movieid*4+2
    m1.add_Shows({"showid": showid, "theaterid":6, "movieid": movieid, "price": 25, "availableSlots": 30 })
    showid=showid+1