# tests/test_api.py
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class LoginAPITestCase(TestCase):
    def setUp(self):
        x = 1
        y = 1
        self.assertEqual(x+y, 2)

    def testcal(self):
        self.assertEqual(1+1, 2);