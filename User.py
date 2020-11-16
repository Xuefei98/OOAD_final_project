from Preference import Preference
class User:
    email = None
    model = None   
    preferenceList = None
    def __init__(self, userID, genre, maxDistance, maxPrice):
        self.email = userID
        self.preferenceList = Preference(genre, maxDistance, maxPrice)
