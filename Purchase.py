class Purchase:
    def __init__(self, purchaseID, movieName, theaterName, moviePrice, foodList):
        self.purchaseID = purchaseID
        self.movieName = movieName
        self.theaterName = theaterName
        self.moviePrice = moviePrice
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
        d['foodList'] = self.foodList
        return d   
