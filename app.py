from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@flaskappcluster.x97xv.mongodb.net/?retryWrites=true&w=majority&appName=FlaskAppCluster")
db = client["shop_db"]
products_collection = db["products"]

mock_data = [{
  "name": "Laptop",
  "tag": "Electronics",
  "price": 899.99,
  "image_path": "images/laptop.jpg"
},
{
  "name": "Coffee Mug",
  "tag": "Kitchenware",
  "price": 12.99,
  "image_path": "images/mug.jpg"
},
{
  "name": "Headphones",
  "tag": "Electronics",
  "price": 199.99,
  "image_path": "images/headphones.jpg"
}]

# Insert mock data into MongoDB collection
products_collection.insert_many(mock_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Fetch products from MongoDB
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
