from flask import Flask, render_template,request
from Model import Model

##--Starting the Web Server--##
app = Flask(__name__)

##-- MVC Pattern --##
class Controller:

    instance=None
    model=None
    port=None

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
    def add_url_rules(self):
        app.add_url_rule('/', 'index', lambda: controller2.hello())
    def hello(self):
        user = self.model.getUser("john@gmail.com") 
        shows = self.model.getShows(user.preferenceList)
        return str(shows[0].price)

if __name__ == "__main__":
    controller1 = Controller()
    controller2 = Controller.getInstance() #Singleton Pattern
    controller2.add_url_rules()
    app.run(host="127.0.0.1",port=5000)