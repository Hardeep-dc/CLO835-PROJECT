import unittest
from unittest.mock import patch, MagicMock
from app import app

class FlaskAppTests(unittest.TestCase):

    @patch('app.db_conn')
    def setUp(self, mock_db):  # Ensure this line is properly indented
        # Mock the database connection
        self.mock_db = mock_db
        self.mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = self.mock_cursor

        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Teardown any resources after tests
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)


    def test_getemp_status_code(self):
        result = self.app.get('/getemp')
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
