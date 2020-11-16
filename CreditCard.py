from Payment import Payment
class CreditCard(Payment):
    def __init__(self, cardNumber, securityCard):
        self.cardNumber = cardNumber
        self.securityCard = securityCard

    def validate(self):
        if self.cardNumber[0] != 0:
            print("Invalid Credit Card Number. Requires 0 as first number.")
        else:
            super(CreditCard, self).validate()
    
    # def generateTicket(self):
    #     super(CreditCard, self).generateTicket()