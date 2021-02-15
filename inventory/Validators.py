from wtforms import ValidationError
from PIL import Image

class UPCValidator():
    field_flags = ('accepts_UPC8, accepts_UPC12, accepts_UPC13, accepts_UPC14, accepts_UPC18')

    def __init__(self, message=None):
        if not message:
            message = "Invalid Universal Product Code(UPC)"
        self.message = message

    def __call__(self, form, field):
        validlengths = [8, 12, 13, 14, 18]
        if len(field.data) not in validlengths:
            raise ValidationError(f"{self.message} (Invalid Length)")
        try:
            lastDigit = int(field.data[-1])  # Get last digit and check if digit is interger
            arr = [int(i) for i in field.data[-2::-1]]  # Convert upc into array
        except ValueError:
            raise ValidationError(f"{self.message} (Invalid Characters in UPC)")
        evenTotal = 0
        oddTotal = 0
        for i, v in enumerate(arr):
            if i % 2 == 0:
                oddTotal += v * 3
            else:
                evenTotal += v
        checkSum = (10 - ((evenTotal + oddTotal) % 10)) % 10
        if checkSum != lastDigit:
            raise ValidationError(f"{self.message} (Invalid checksum {checkSum} got {lastDigit})")


class ImageValidator():
    field_flags = ('accepts_IMAGES')

    def __init__(self, message=None):
        if not message:
            self.message = "Invalid image file."

    def __call__(self, form, field):
        try:
            f = Image.open(field.data)
            f = f.convert("RGB")
        except Image.UnidentifiedImageError:
            raise ValidationError(self.message)


class LessThan(object):
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data is not None:
            if field.data <= other.data:
                d = {
                    'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                    'other_name': self.fieldname
                }
                message = self.message
                if message is None:
                    message = field.gettext('Field must be less than %(other_name)s.')
                raise ValidationError(message % d)
