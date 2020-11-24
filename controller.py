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

    def add_url_rules(self):
        app.add_url_rule('/', 'index', lambda: controller2.index())
        app.add_url_rule('/login', 'login', lambda: controller2.login(), methods=['POST'])
        app.add_url_rule('/signUp', 'signUp', lambda: controller2.signUp(), methods=['POST','GET'])
        app.add_url_rule('/signOut', 'signOut', lambda: controller2.signOut(), methods=['POST'])
        app.add_url_rule('/shows', 'shows', lambda: controller2.shows(), methods=['POST', 'GET'])
        app.add_url_rule('/show', 'show', lambda: controller2.show(), methods=['POST', 'GET'])
        app.add_url_rule('/dashboard', 'dashboard', lambda: controller2.dashboard(), methods=['POST', 'GET'])
        app.add_url_rule('/purchase', 'purchase', lambda: controller2.purchase(), methods=['POST', 'GET'])
        app.add_url_rule('/cancelPurchase', 'cancelPurchase', lambda: controller2.cancelPurchase(), methods=['POST', 'GET'])
        app.add_url_rule('/updatePreferences', 'updatePreferences', lambda: controller2.updatePreferences(), methods=['POST','GET'])

    def index(self):
        return render_template('home.html')

    def login(self):
        if request.method == 'POST':
            s = Context(SignIn())
            params = dict()
            params['username'] = request.form.get('username')
            params['password'] = request.form.get('password')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params)
            return redirect(url_for('dashboard'))
            #return redirect(url_for('shows'))
        return "logged in"

    def signUp(self):
        if request.method == 'GET':
           return render_template('signup.html')
        if request.method == 'POST':
            s = Context(SignUp())
            params = dict()
            params['email'] = request.form.get('username')
            params['password'] = request.form.get('password')
            params['genre'] = request.form.get('genre')
            params['maxDistance'] = request.form.get('maxDistance')
            params['maxPrice'] = request.form.get('maxPrice')
            self.session = s.getStrategy.handleActivity(self.session, self.model, params)
            return redirect(url_for('dashboard'))
            #return redirect(url_for('shows'))
        return "logged in"

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
                e['foodQuantity'] = 0
                d['foodList'].append(e)
            #randomlize a purchase id
            #add movie and food list to the database
            self.purchaseID=random.randint(10000,900000)
            self.purchaseInfo=dict()
            self.purchaseInfo['purchaseID']=self.purchaseID
            self.purchaseInfo['username']=self.session['username']
            self.purchaseInfo['movieName']=d['movieName']
            self.purchaseInfo['moviePrice']=d['price']
            self.purchaseInfo['availableFoodList']=d['foodList']
            self.purchaseInfo['foodList']=[]
            self.purchaseInfo['theaterName']=d['theaterName']
            res.append(d)
            return jsonify(res)

        if request.method == 'POST':
            num_slots = request.args.get('num_slots')
            i=0
            for item in self.purchaseInfo['availableFoodList']:
                print(item)
                item['foodQuantity'] = int(request.args.get('food_quantity_list:'+str(i)))
                if(item['foodQuantity']>0):
                    e=dict()
                    e['foodName']=item['foodName']
                    e['foodQuantity']=item['foodQuantity']
                    self.purchaseInfo['foodList'].append(e)
                i=i+1
            sum= 0
            for item in self.purchaseInfo['availableFoodList']:
                sum+= item['foodQuantity']*item['foodprice']
            total=sum+ int(num_slots) * self.purchaseInfo['moviePrice']
            return jsonify(total)

    def purchase(self):
        if request.method == 'POST':
            cardNumber = request.args.get('cardNumber')
            securityCode = request.args.get('securityCode')
            expireDate = request.args.get('expireDate')
            cardType= request.args.get('cardType')
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
        return "updated the purchase info"

    def cancelPurchase(self):
        if request.method == 'POST':
            choose_index = int(request.args.get('index'))
            purchaseID= self.session['user'].purchaseList[choose_index].getPurchaseDetails()['purchaseID']
            self.model.deletePurchaseRecord(purchaseID)
            return redirect(url_for('dashboard'))
        return "cancel Purchase"

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