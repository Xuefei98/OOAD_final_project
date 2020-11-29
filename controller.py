from flask import Flask, render_template,request,redirect,url_for,jsonify
from Model import Model
from Context import Context
from SignIn import SignIn
from SignUp import SignUp
import random
from CreditCard import CreditCard
from DebitCard import DebitCard

##--Starting the Web Server--##
app = Flask(__name__)

##-- MVC Pattern --##
class Controller:

    instance=None
    model=None
    session=None
    showsRes=None
    purchaseList=None
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
    ##-- Add API end points --##        
    def add_url_rules(self):
        app.add_url_rule('/', 'index', lambda: controller2.index())
        app.add_url_rule('/login', 'login', lambda: controller2.login(), methods=['POST'])
        app.add_url_rule('/signUp', 'signUp', lambda: controller2.signUp(), methods=['POST','GET'])
        app.add_url_rule('/signOut', 'signOut', lambda: controller2.signOut(), methods=['GET'])
        app.add_url_rule('/shows', 'shows', lambda: controller2.shows(), methods=['POST', 'GET'])
        app.add_url_rule('/show', 'show', lambda: controller2.show(), methods=['POST', 'GET'])
        app.add_url_rule('/dashboard', 'dashboard', lambda: controller2.dashboard(), methods=['POST', 'GET'])
        app.add_url_rule('/purchase', 'purchase', lambda: controller2.purchase(), methods=['POST', 'GET'])
        app.add_url_rule('/cancelPurchase', 'cancelPurchase', lambda: controller2.cancelPurchase(), methods=['POST', 'GET'])
        app.add_url_rule('/updatePreferences', 'updatePreferences', lambda: controller2.updatePreferences(), methods=['POST','GET'])
    ##-- Render landing index page --##    
    def index(self):
        return render_template('home.html')
    ##-- Login controller function --##
    def login(self):
        if request.method == 'POST':
            ##-- Strategy Pattern --##
            s = Context(SignIn())
            params = dict()
            params['username'] = request.form.get('username')
            params['password'] = request.form.get('password')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params)
            return redirect(url_for('shows'))
            #return redirect(url_for('updatePreferences'))
        return "logged in"
    ##-- Sign Up controller function --##
    def signUp(self):
        if request.method == 'GET':
           return render_template('signup.html')
        if request.method == 'POST':
            ##-- Strategy Pattern --##
            s = Context(SignUp())
            params = dict()
            params['email'] = request.form.get('username')
            params['password'] = request.form.get('password')
            params['genre'] = request.form.get('genre')
            params['maxDistance'] = request.form.get('maxDistance')
            params['maxPrice'] = request.form.get('maxPrice')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params)
            return redirect(url_for('shows'))
            #return redirect(url_for('updatePreferences'))
        return "logged in"
    ##-- Dashboard controller function --##
    def dashboard(self):
        if request.method == 'GET':
            d = dict()
            email = self.session['username']
            self.session['user'] = self.model.getUser(email)
            userPreferences= self.session['user'].preferenceList.getPreferences()
            d['genre'] = userPreferences['genre']
            d['maxDistance'] = userPreferences['maxDistance']
            d['maxPrice'] = userPreferences['maxPrice']
            d['purchaseList'] = []
            for item in self.session['user'].purchaseList:
                d['purchaseList'].append(item.getPurchaseDetails())
            return render_template('dashboard.html', userInfo=d)
        return "dashboard"
    ##-- Update Preferences controller function --##
    def updatePreferences(self):
        if request.method == 'GET':
            return render_template('preferences.html')
        if request.method == 'POST':
            newGenre = request.form.get('genre')
            newDistance = request.form.get('maxDistance')
            newPrice = request.form.get('maxPrice')
            print(newGenre)
            self.session['user']= self.model.updatePreferences(self.session['username'],newGenre,newDistance,newPrice)
            return redirect(url_for('dashboard'))
        return "updated page"
    ##-- Get currently playing shows matching preferences controller function --##
    def shows(self):
        res= []
        if request.method == 'GET':
            self.showsRes= self.model.getShows(self.session['user'].preferenceList.getPreferences())
            i=0
            for item in self.showsRes:
                d = dict()
                d['theaterName'] = item.getShowDetails()['theater'].getTheaterDetails()['theaterName']
                d['movieName'] = item.getShowDetails()['movie'].getMovieDetails()['movieName']
                d['price'] = item.getShowDetails()['price']
                d['index'] = i
                i= i+1
                res.append(d)
        # return jsonify(res)
        return render_template('shows.html', userShows=res)
    ##--- Book the show with food add-ons controller function --##
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
            d['slots'] = 0
            d['totalCost'] = 0
            d['foodList'] = []
            for foodItem in item.getShowDetails()['theater'].getTheaterDetails()['foodList']:
                e = dict()
                e['foodName'] = foodItem.getFoodDetails()['foodName']
                e['foodprice'] = foodItem.getFoodDetails()['foodprice'] 
                e['foodQuantity'] = 0
                d['foodList'].append(e)
            #randomize a purchase id
            #add movie and food list to the database
            self.purchaseID=random.randint(10000,900000)
            self.purchaseInfo=dict()
            self.purchaseInfo['purchaseID']=self.purchaseID
            self.purchaseInfo['username']=self.session['username']
            self.purchaseInfo['movieName']=d['movieName']
            self.purchaseInfo['moviePrice']=d['price']
            self.purchaseInfo['slots']=d['slots']
            self.purchaseInfo['availableFoodList']=d['foodList']
            self.purchaseInfo['foodList']=[]
            self.purchaseInfo['theaterName']=d['theaterName']
            self.purchaseInfo['totalCost']=d['totalCost']
            res.append(d)
            # return jsonify(res)
            return render_template('show.html', showInfo=d)

        if request.method == 'POST':
            self.purchaseInfo['slots'] = request.form.get('slots')
            i=0
            for item in self.purchaseInfo['availableFoodList']:
                print(request.form.get(item['foodName']))
                item['foodQuantity'] = int(request.form.get(item['foodName']))
                if(item['foodQuantity']>0):
                    e=dict()
                    e['foodName']=item['foodName']
                    e['foodQuantity']=item['foodQuantity']
                    self.purchaseInfo['foodList'].append(e)
                i=i+1
            sum= 0
            for item in self.purchaseInfo['availableFoodList']:
                sum+= item['foodQuantity']*item['foodprice']
            self.purchaseInfo['totalCost']=sum+ int(self.purchaseInfo['slots']) * self.purchaseInfo['moviePrice']
            return redirect(url_for('purchase'))
    ##-- Payment controller function --##
    def purchase(self):
        if request.method == 'GET':
           d = dict() 
           d['totalCost'] = self.purchaseInfo['totalCost']
           return render_template('purchase.html', purchaseInfo=d)
        if request.method == 'POST':
            cardNumber = request.form.get('cardNumber')
            securityCode = request.form.get('securityCode')
            expireDate = request.form.get('expireDate')
            cardType= request.form.get('cardType')
            ##-- Template Pattern --##
            if cardType == "credit":
                payPass = CreditCard(cardNumber,securityCode,expireDate).PaymentSummary()
            else:
                payPass = DebitCard(cardNumber,securityCode,expireDate).PaymentSummary()
            if payPass == 1:
                self.purchaseInfo['cardNumber']=cardNumber
                self.purchaseInfo['expireDate']=expireDate
                self.model.addPurchase(self.purchaseInfo)
            else:
                print("Sorry your card did not go through the system")
            return redirect(url_for('dashboard'))
    ##-- Cancel previous purchase controller function --##
    def cancelPurchase(self):
        if request.method == 'GET':
            purchaseID = int(request.args.get('index'))
            self.model.deletePurchaseRecord(purchaseID)
            return redirect(url_for('dashboard'))
        return "cancel Purchase"

    ##-- Sign Out controller function --##
    def signOut(self):
        self.session= None
        self.session= dict()
        self.purchaseInfo= dict()
        return redirect(url_for('index'))

if __name__ == "__main__":
    controller1 = Controller()
    controller2 = Controller.getInstance() #Singleton Pattern
    controller2.add_url_rules()
    app.run(host="127.0.0.1",port=5000)