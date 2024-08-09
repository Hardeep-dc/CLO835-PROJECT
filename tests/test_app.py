import unittest
from app import app
from flask import url_for
import os

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Teardown any resources after tests
        pass

    def test_home_status_code(self):
        # Test the status code of the home page
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        # Test the status code of the about page
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_getemp_status_code(self):
        # Test the status code of the get employee page
        result = self.app.get('/getemp')
        self.assertEqual(result.status_code, 200)



if __name__ == "__main__":
    unittest.main()
