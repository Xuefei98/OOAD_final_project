from Strategy import Strategy
class SignUp(Strategy):
    def handleActivity(self, session, model, params):
        model.addUser({"email": params['email'], "password": params['password'], "genre": params['genre'], "maxDistance": params['maxDistance'], "maxPrice": params['maxPrice']})
        session['user'] = model.getUser(params['email'])
        session['username'] = params['email']
        return session