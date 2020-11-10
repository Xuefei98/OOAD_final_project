from Movie import Movie
from Theater import Theater
class Show:
    def __init__(self, d):
        self.movie = Movie( d['movieName'], d['duration'], d['genre'], d['movieid'])
        self.theater = Theater(d['theaterName'], d['distance'], d['theaterid'], d['foodList'])
        self.price = d['price']    
    def getShowDetails(self):
        d = dict()
        d['movie'] = self.movie
        d['theater'] = self.theater
        d['price'] = self.price
        return d   
        