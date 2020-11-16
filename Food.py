class Food:
    def __init__(self, foodid, name, price):
        self.foodid = foodid
        self.name = name
        self.price = price
        
    def getFoodDetails(self):
        d = dict()
        d['foodid'] = self.foodid
        d['foodName'] = self.name
        d['foodprice'] = self.price
        return d   
