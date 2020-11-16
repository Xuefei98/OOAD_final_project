from Payment import Payment
class CreditCard(Payment):
    def __init__(self, cardNumber, securityCard):
        self.cardNumber = cardNumber
        self.securityCard = securityCard

    def validate(self):
        if len(self.cardNumber) != 10:
            print("Needs 10 numbers")
        else:
            super(DebitCard, self).validate()
    
    def generateTicket(self):
        super(DebitCard, self).generateTicket()