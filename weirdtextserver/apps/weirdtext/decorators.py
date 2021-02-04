"""File contains decorators for weirdtext app views"""
from django.http.response import JsonResponse


def exception_guard(func):
    """
    Decorator is catching ValueError exception while executing decoding action in application view.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            return JsonResponse({"error": "Could not decode the message", "error_type": e.args[1]})

    return wrapper
