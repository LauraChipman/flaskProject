import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class TestDatabaseWrite(unittest.TestCase):
    """Tests for MongoDB write operations"""

    def setUp(self):
        # Load environment variables
        load_dotenv()
        self.client = MongoClient(
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@flaskappcluster.x97xv.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client['shop_db']
        self.collection = self.db['products']

    def test_insert_document(self):
        """Test inserting a document into MongoDB"""
        test_product = {
            "name": "Test Product",
            "tag": "Testing",
            "price": 0.99,
            "image_path": "images/test.jpg"
        }
        # Insert the document
        result = self.collection.insert_one(test_product)
        self.assertIsNotNone(result.inserted_id)

        # Verify the document exists
        retrieved_product = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(retrieved_product)


if __name__ == '__main__':
    unittest.main()
