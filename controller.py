from flask import Flask, render_template,request,redirect,url_for,jsonify
from Model import Model
from Context import Context
from SignIn import SignIn
from SignUp import SignUp
##--Starting the Web Server--##
app = Flask(__name__)

##-- MVC Pattern --##
class Controller:

    instance=None
    model=None
    session=None
    showsRes=None
    ##-- Singleton Pattern --##
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Controller.instance == None:
            Controller()
        return Controller.instance

    def __init__(self):
        """ Virtually private constructor. """
        if Controller.instance != None:
            raise Exception("This class is a singleton!")
        else:
            Controller.instance = self
            Controller.model = Model()
            Controller.session = dict()
    def add_url_rules(self):
        app.add_url_rule('/', 'index', lambda: controller2.index())
        app.add_url_rule('/login', 'login', lambda: controller2.login(), methods=['POST'])
        app.add_url_rule('/signUp', 'signUp', lambda: controller2.signUp(), methods=['POST'])
        app.add_url_rule('/signOut', 'signOut', lambda: controller2.signOut(), methods=['POST'])
        app.add_url_rule('/shows', 'shows', lambda: controller2.shows(), methods=['POST', 'GET'])
        app.add_url_rule('/show', 'show', lambda: controller2.show(), methods=['POST', 'GET'])
        app.add_url_rule('/dashboard', 'dashboard', lambda: controller2.dashboard(), methods=['POST', 'GET'])
        app.add_url_rule('/updatePreferences', 'updatePreferences', lambda: controller2.updatePreferences(), methods=['POST'])
    def index(self):
        return "Drive and Reel"
    def login(self):
        if request.method == 'POST':
            s = Context(SignIn())
            params = dict()
            params['username'] = request.args.get('username')
            params['password'] = request.args.get('password')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params) 
            return redirect(url_for('shows'))
        return "logged in"
    def signUp(self):
        if request.method == 'POST':
            s = Context(SignUp())
            params = dict()
            params['email'] = request.args.get('email')
            params['password'] = request.args.get('password')
            params['genre'] = request.args.get('genre')
            params['maxDistance'] = request.args.get('maxDistance')
            params['maxPrice'] = request.args.get('maxPrice')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params) 
            return redirect(url_for('shows'))
        return "logged in"
    def dashboard(self):
        if request.method == 'GET':
            return jsonify(self.session['user'].preferenceList.getPreferences())
        return "dashboard"
    def updatePreferences(self):
        if request.method == 'POST':
            newGenre= request.args.get('genre')
            newDistance= request.args.get('maxDistance')
            newPrice= request.args.get('maxPrice')
            print(newGenre)
            self.session['user']= self.model.updatePreferences(self.session['username'],newGenre,newDistance,newPrice)
            return redirect(url_for('dashboard'))
        return "updated page"
    def shows(self):
        res= []
        if request.method == 'GET':
            self.showsRes= self.model.getShows(self.session['user'].preferenceList.getPreferences())
            for item in self.showsRes:
                d = dict()
                d['theaterName'] = item.getShowDetails()['theater'].getTheaterDetails()['theaterName']
                d['movieName'] = item.getShowDetails()['movie'].getMovieDetails()['movieName']
                d['price'] = item.getShowDetails()['price']
                res.append(d)
        return jsonify(res) 
    def show(self):
        res= []
        if request.method == 'GET':
            index= int(request.args.get('index'))
            print("index")
            print(index)
            item= self.showsRes[index]
            d = dict()
            d['theaterName'] = item.getShowDetails()['theater'].getTheaterDetails()['theaterName']
            d['distance'] = item.getShowDetails()['theater'].getTheaterDetails()['distance']
            d['movieName'] = item.getShowDetails()['movie'].getMovieDetails()['movieName']
            d['genre'] = item.getShowDetails()['movie'].getMovieDetails()['genre']
            d['price'] = item.getShowDetails()['price']
            d['foodList'] = []
            for foodItem in item.getShowDetails()['theater'].getTheaterDetails()['foodList']:
                e = dict()
                e['foodName'] = foodItem.getFoodDetails()['foodName']
                e['foodprice'] = foodItem.getFoodDetails()['foodprice']  
                d['foodList'].append(e)    
            res.append(d)
        return jsonify(res)  
    def signOut(self):
        self.session= None
        self.session= dict()
        return redirect(url_for('index'))

if __name__ == "__main__":
    controller1 = Controller()
    controller2 = Controller.getInstance() #Singleton Pattern
    controller2.add_url_rules()
    app.run(host="127.0.0.1",port=5000)