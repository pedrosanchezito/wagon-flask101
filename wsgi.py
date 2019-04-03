# wsgi.py
from flask import Flask, jsonify, request
import json
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


@app.route('/api/v1/products', methods = ['GET','POST'])
def get_products():
    if request.method == 'GET':
        return jsonify(PRODUCTS), 200

    if request.method == 'POST':
        name = json.dumps(request.get_json())
        PRODUCTS.append({'id':ID.next(), 'name':name})
        return "Product created", 201

    return "", 404



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
                return "Product deleted", 204

    return "This product does not exist", 404


class Counter:
    def __init__(self):
        self.id = 4

    def next(self):
        self.id += 1
        return self.id

ID = Counter()
