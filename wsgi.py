# wsgi.py
from flask import Flask, jsonify, request
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Youtube' },
    { 'id': 4, 'name': 'Twitch' }
]


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    return jsonify(PRODUCTS), 200

@app.route('/api/v1/products/<int:id>', methods = ['GET','DELETE'])
def manage_product(id):
    if request.method == 'GET':
        for product in PRODUCTS:
            if product['id'] == id:
                return jsonify(product), 200

    if request.method == 'DELETE':
        for product in PRODUCTS:
            if product['id'] == id:
                PRODUCTS.remove(product)
                return "Produit supprimé", 204

    return "Ce produit n'existe pas", 404
