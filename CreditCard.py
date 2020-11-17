from Payment import Payment
class CreditCard(Payment):
    def __init__(self, cardNumber, securityCode,expireDate):
        self.cardNumber = cardNumber
        self.securityCode = securityCode
        self.expireDate = expireDate

    def validate(self):
        if self.cardNumber[0] != '0':
            return 0
            print("Invalid Credit Card Number. Requires 0 as first number.")
        else:
            return 1

