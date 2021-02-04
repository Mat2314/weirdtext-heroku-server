from django.test import TestCase
from rest_framework.test import APIClient


class UserUnauthenticatedTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_encode(self):
        """Test checks connection to encode endpoint and result of encoding"""
        response = self.client.post('/v1/encode/', {'message': 'This is Sparta!'})
        # Check if client got connected
        self.assertEqual(response.status_code, 200)

        # Check if response content is adequate
        self.assertEqual(response.json()['ok'], 'Successfully encoded the message')
        self.assertTrue('encoded_message' in response.json())
        self.assertTrue('original_words' in response.json())

    def test_decoding_error(self):
        """Test checks decode endpoint behavior on error"""
        weirdtext = "Tihs is Sptara!"
        original_words = "Not,this,time".split(',')

        response = self.client.post('/v1/decode/', {'weirdtext': weirdtext, 'original_words': original_words})
        # Check if client got connected
        self.assertEqual(response.status_code, 200)

        # Check returned values on error response
        self.assertEqual(response.json()['error'], 'Could not decode the message')
        self.assertTrue('error_type' in response.json())
