from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL
from SingleTonPattern.product import Product

app = Flask(__name__)

# db configuration

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos'

mysql = MySQL(app)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/api/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    profile = request.form['profile']

    new_product = Product(mysql).get_instance()
    new_product.insert_product(name,price,profile,quantity)

    data = {'message': 'Saved successfuly'}
    return jsonify(data)


@app.route('/api/products')
def products():
    product = Product(mysql).get_instance()
    products_list = product.get_products()

    return jsonify(products_list)


@app.route('/api/search', methods=['POST'])
def search():
    querry = request.form['querry']

    product = Product(mysql).get_instance()
    products_list = product.find_products(querry)
    
    return jsonify(products_list)


if __name__ == "__main__":
    app.run(debug=True)
