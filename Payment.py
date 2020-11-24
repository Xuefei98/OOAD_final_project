##-- Template Pattern --##
class Payment:

    def __init__(self, cardNumber, securityCode, expireDate):
        self.cardNumber = cardNumber
        self.securityCode = securityCode
        self.expireDate=expireDate

    def validate(self):
        pass

    def PaymentSummary(self):
        print('card number is ', self.cardNumber)
        print('CVC number is  ', self.securityCode)
        print('expire date is ', self.expireDate)
        print('validate',self.validate())
        return self.validate()