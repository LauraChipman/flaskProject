import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class TestDatabaseRead(unittest.TestCase):
    """Tests for MongoDB read operations"""

    def setUp(self):
        # Load environment variables
        load_dotenv()
        self.client = MongoClient(
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@flaskappcluster.x97xv.mongodb.net/?retryWrites=true&w=majority"
        )

    def test_ping_database(self):
        """Test that MongoDB connection is successful"""
        try:
            # Ping the database
            self.client.admin.command('ping')
        except Exception as e:
            self.fail(f"Database connection failed: {e}")
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
