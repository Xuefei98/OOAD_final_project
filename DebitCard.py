from Payment import Payment
class DebitCard(Payment):
    def __init__(self, cardNumber, securityCode):
        self.cardNumber = cardNumber
        self.securityCode = securityCode
    
    def validate(self):
        if self.cardNumber[0] != 1:
            print("Invalid Debit Card Number. Requires 1 as first number.")
        else:
            super(DebitCard, self).validate()
    
    # def generateTicket(self):
    #     super(DebitCard, self).generateTicket()