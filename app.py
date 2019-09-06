from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'pizzadb'
app.config['MONGO_URI'] = 'mongodb://adi_tdkr:adityatodkar24@ds259410.mlab.com:59410/pizzadb'

mongo = PyMongo(app)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    pizzaList = mongo.db.pizza.find()
    return dumps(pizzaList)

if __name__ == '__main__':
    app.run(debug=True)