# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Lolilol' },
]


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>', methods = ['GET','POST'])
def get_product(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return jsonify(product)
    return "Ce produit n'existe pas", 404


