import os
from django.test import TestCase
from django.conf import settings 
from django.contrib.auth.password_validation import validate_password


class CustomTest(TestCase):
    # https://docs.python.org/3/library/unittest.html  ==> python library for test
    def test_secret_key_strength(self):
        SECRET_KEY = settings.SECRET_KEY
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'secret key is very weak: {e.messages}'
            self.fail(msg)
    