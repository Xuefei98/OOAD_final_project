class Show:
    def __init__(self, movie, theater, price):
        self.movie = movie
        self.theater = theater
        self.price = price
    """    
    def getShowDetails(self):
        d = dict()
        movie = self.model.getMovie(self.movieid)
        d['movieName'] = movie.name
        d['duration'] = movie.duration
        theater = self.model.getTheater(self.theaterid)
        d['theaterName'] = theater.name
        d['distance'] = theater.distance
        d['price'] = self.price
        return d   
   """    
        