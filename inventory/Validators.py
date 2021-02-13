from wtforms import ValidationError


class UPCValidator():
    field_flags = ('accepts_UPC8, accepts_UPC12, accepts_UPC13, accepts_UPC14, accepts_UPC18')

    def __init__(self, message=None):
        if not message:
            message = "Invalid Universal Product Code(UPC)"
        self.message = message

    def __call__(self, form, field, message=None):
        validlengths = [8, 12, 13, 14, 18]
        if len(field.data) not in validlengths:
            raise ValidationError(message)
        try:
            lastDigit = int(field.data[-1])  # Get last digit and check if digit is interger
            arr = [int(i) for i in field.data[-2::-1]]  # Convert upc into array
        except ValueError:
            raise ValidationError(message)
        evenTotal = 0
        oddTotal = 0
        for i, v in enumerate(arr):
            if i % 2 == 0:
                oddTotal += v * 3
            else:
                evenTotal += v
        checkSum = (10 - ((evenTotal + oddTotal) % 10)) % 10
        if checkSum != lastDigit:
            raise ValidationError(message)
