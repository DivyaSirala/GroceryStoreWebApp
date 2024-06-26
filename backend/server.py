from flask import Flask, request, jsonify
import products_dao
import uom_dao
from sql_connection import get_sql_connection

app = Flask(__name__)       #Started a Flask application on local computer port=5000

#Creating a global varibale
connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_products():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#Getting UOMs
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#INSERTING A NEW PRODUCT TO THE DB
@app.route('/insertProduct', methods=['POST'])
def insert_products():
    request_payload = request.form['data']
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(port=5000)

