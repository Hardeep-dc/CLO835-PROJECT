import unittest
from unittest.mock import patch, MagicMock
from app import app

class FlaskAppTests(unittest.TestCase):

    @patch('app.db_conn')  # This mocks the db_conn in the app module
    def setUp(self, mock_db):
        # Mock the database connection and cursor
        self.mock_db = mock_db
        self.mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = self.mock_cursor

        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
