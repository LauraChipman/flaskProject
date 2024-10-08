from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__, template_folder ="templates")

client = MongoClient("mongodb+srv://dbUser:P94csSBhhiU2eA.@flaskappcluster.x97xv.mongodb.net/?retryWrites=true&w=majority&appName=FlaskAppCluster")
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

products_collection.insert_many(mock_data)
# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Products route
@app.route('/products')
def products():
    # Fetch products from MongoDB
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
