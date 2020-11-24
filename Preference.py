##-- Class to store and fetch preference details of preference object --##
class Preference:
    def __init__(self, genre, maxDistance, maxPrice):
        self.genre = genre
        self.maxDistance = maxDistance
        self.maxPrice = maxPrice
    def getPreferences(self):
        d = dict()
        d['genre'] = self.genre
        d['maxDistance'] = self.maxDistance
        d['maxPrice'] = self.maxPrice
        return d
