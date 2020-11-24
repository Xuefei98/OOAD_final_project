from Strategy import Strategy

##-- Strategy Pattern --##
class SignUp(Strategy):
    def handleActivity(self, session, model, params):
        model.addUser({"email": params['email'], "password": params['password'], "genre": params['genre'], "maxDistance": params['maxDistance'], "maxPrice": params['maxPrice']})
        session['user'] = model.getUser(params['email'])
        session['username'] = params['email']
        return session