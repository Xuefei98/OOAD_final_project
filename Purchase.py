##-- Class to store and fetch purchase details of purchase object --##
class Purchase:
    def __init__(self, purchaseID, movieName, theaterName, moviePrice, movieSlots, foodList):
        self.purchaseID = purchaseID
        self.movieName = movieName
        self.theaterName = theaterName
        self.moviePrice = moviePrice
        self.movieSlots = movieSlots
        res= []
        for item in foodList:
            res.append(str(item['foodName'])+":"+str(item['foodQuantity']))
        self.foodList= res    
        
    def getPurchaseDetails(self):
        d = dict()
        d['purchaseID'] = self.purchaseID
        d['movieName'] = self.movieName
        d['theaterName'] = self.theaterName
        d['moviePrice'] = self.moviePrice
        d['movieSlots'] = self.movieSlots
        d['foodList'] = self.foodList
        return d   
