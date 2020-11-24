##-- Class to store and fetch movie details of movie object --##
class Movie:
    def __init__(self, movieName, duration, genre, movieid):
        self.movieid = movieid
        self.name = movieName
        self.genre = genre
        self.duration = duration
        
    def getMovieDetails(self):
        d = dict()
        d['movieName'] = self.name
        d['duration'] = self.duration
        d['genre'] = self.genre
        d['movieid'] = self.movieid
        return d   
