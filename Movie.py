class Movie:
    def __init__(self, movieid, name, genre, duration):
        self.movieid = movieid
        self.name = name
        self.genre = genre
        self.duration = duration
        
    def getMovieDetails(self):
        d = dict()
        d['movieName'] = self.name
        d['duration'] = self.duration
        d['genre'] = self.genre
        d['movieid'] = self.movieid
        return d   
        