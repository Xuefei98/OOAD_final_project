from Payment import Payment
class DebitCard(Payment):
    def __init__(self, cardNumber, securityCode, expireDate):
        self.cardNumber = cardNumber
        self.securityCode = securityCode
        self.expireDate = expireDate

    def validate(self):
        if self.cardNumber[0] != 1:
            return 0
            print("Invalid Debit Card Number. Requires 1 as first number.")
        else:
            return 1
