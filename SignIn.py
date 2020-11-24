from Strategy import Strategy

##-- Strategy Pattern --##
class SignIn(Strategy):
    def handleActivity(self, session, model, params):
        password= model.getCredentials(params['username'])
        if(password == params['password']):    
            session['user'] = model.getUser(params['username'])
            session['username'] = params['username']
            return session
        else:
           return None