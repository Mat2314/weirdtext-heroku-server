from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .utils.weirdtext_decoder import decode
from .utils.weirdtext_encoder import encode


# Create your views here.
class EncodeViewSet(viewsets.ViewSet):
    """
    A simple viewset for encoding messages to weirdtext.
    """

    def create(self, request):
        """
        Endpoint transforms text to a weirdtext value.
        Expected payload:
        - message: string
        """
        message = encode(request.data['message'])
        return JsonResponse(
            {"ok": "Successfully encoded the message", "encoded_message": message[0], "original_words": message[1]})


class DecodeViewSet(viewsets.ViewSet):
    """
    A simple viewset for decoding messages from weirdtext to original form.
    """

    def create(self, request):
        """
        Endpoint transforms weirdtext value to original message.
        Expected payload:
        - weirdtext: string
        - original_words: list
        """
        try:
            message = decode(request.data['weirdtext'], request.data['original_words'])
            return JsonResponse({"ok": "Successfully decoded the message", "decoded_message": message})
        except ValueError as e:
            print(e)
            return JsonResponse({"error": "Could not decode the message", "error_type": e.args[1]})
