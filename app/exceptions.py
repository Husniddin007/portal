from django.db.models import IntegerChoices
from rest_framework.exceptions import APIException

class ErrorCodes(IntegerChoices):
    OBJECT_NOT_FOUND = 400_001

def error_exception(ExceptionClass,error_code=ErrorCodes) -> APIException:
    exception = ExceptionClass({
        'error_code':error_code
    })
    return exception