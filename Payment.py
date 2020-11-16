class Payment:
    """
    validate func from:
    https://blog.tecladocode.com/python-30-day-9-project/
    """
    def validate(self):
        validateCardNum = list((self.cardNumber).strip())
        # pop off check digit
        checkDigit = validateCardNum.pop()
        # reverse order of remaining numbers
        validateCardNum.reverse()

        finishedDigits = []

        for i, digit in enumerate(validateCardNum):
            if i % 2 == 0:
                doulbed = int(digit) * 2

                # subtract 9 if product over 9
                if doubled > 9:
                    doulbed -= 9
                
                finishedDigits.append(doubled)
            else:
                finishedDigits.append(int(digit))
        
        total = int(checkDigit) + sum(finishedDigits)

        if total % 10 == 0:
            return True
        else:
            return False

    def generateTicket(self):
        # QUESTIONABLE TODO
        