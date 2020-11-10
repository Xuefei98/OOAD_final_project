from Food import Food
class Theater:
    def __init__(self, theaterName, distance, theaterid, foodList):
        self.theaterid = theaterid
        self.name = theaterName
        self.distance = distance
        res= []
        for item in foodList:
            res.append(Food(item['foodid'],item['foodName'],item['foodprice']))
        self.foodList= res    
        
    def getTheaterDetails(self):
        d = dict()
        d['theaterName'] = self.name
        d['distance'] = self.distance
        d['theaterid'] = self.theaterid
        d['foodList'] = self.foodList
        return d   
        