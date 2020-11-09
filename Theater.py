class Theater:
    def __init__(self, theaterid, name, distance, foodList):
        self.theaterid = theaterid
        self.name = name
        self.distance = distance
        self.foodList = foodList
        
    def getTheaterDetails(self):
        d = dict()
        d['theaterName'] = self.name
        d['distance'] = self.distance
        d['theaterid'] = self.theaterid
        return d   
        