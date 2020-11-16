from Payment import Payment
class DebitCard(Payment):
    def __init__(self, cardNumber, securityCode):
        self.cardNumber = cardNumber
        self.securityCode = securityCode
    
    def validate(self):
        if len(self.cardNumber) != 10:
            print("Needs 10 numbers")
        else:
            super(DebitCard, self).validate()
    
    def generateTicket(self):
        super(DebitCard, self).generateTicket()