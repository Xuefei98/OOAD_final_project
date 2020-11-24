##-- Class to store and fetch user details of user object --##
from Preference import Preference
from Purchase import Purchase
class User:
    email = None
    model = None   
    preferenceList = None
    purchaseList= None
    def __init__(self, userID, genre, maxDistance, maxPrice, purchaseList):
        self.email = userID
        self.preferenceList = Preference(genre, maxDistance, maxPrice)
        res= []
        for item in purchaseList:
            res.append(Purchase(item['purchaseID'],item['movieName'],item['theaterName'],item['moviePrice'],item['foodList']))
        self.purchaseList= res    
