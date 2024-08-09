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

    def test_addemp_route(self):
        # Test the add employee route with valid data
        result = self.app.post('/addemp', data={
            'emp_id': '1',
            'first_name': 'John',
            'last_name': 'Doe',
            'primary_skill': 'Python',
            'location': 'New York'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'John Doe', result.data)

    def test_getemp_status_code(self):
        # Test the status code of the get employee page
        result = self.app.get('/getemp')
        self.assertEqual(result.status_code, 200)

    def test_fetchdata_route(self):
        # Test the fetch data route with a valid employee ID
        result = self.app.post('/fetchdata', data={'emp_id': '1'})
        self.assertEqual(result.status_code, 200)

    def test_invalid_color(self):
        # Simulate passing an unsupported color to test error handling
        with self.assertRaises(SystemExit) as cm:
            os.environ['APP_COLOR'] = 'unsupported_color'
            app.run()
        self.assertEqual(cm.exception.code, 1)

if __name__ == "__main__":
    unittest.main()
