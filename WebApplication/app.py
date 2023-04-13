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
product = Product(mysql).get_instance()

@app.route('/')
def home_page():
    return render_template('login.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dash.html')

@app.route('/sales')
def sales_page():
    return render_template('sales.html')

@app.route('/manageproducts')
def manageproducts_page():
    return render_template('manageproducts.html')


@app.route('/api/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    product.insert_product(name,price,profile,quantity)

    data = {'message': 'Saved successfuly'}
    return jsonify(data)


@app.route('/api/products')
def products():
    products_list = product.get_products()

    return jsonify(products_list)

@app.route('/api/search', methods=['POST'])
def search():
    querry = request.form['querry']

    products_list = product.find_products(querry)
    
    return jsonify(products_list)

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    product_name = request.form['product_name']
    product_price = request.form['product_price']
    product_quantity = request.form['product_quantity']
    product_profile = request.form['product_profile']

    product = {'id': product_id, 'name': product_name, 'price': product_price,
               'quantity': product_quantity, 'profile': product_profile}

    Cart.get_instance().add_product(product)

    return jsonify({'message': 'Added to cart'})


@app.route('/cart')
def cart():
    # Sample cart data

    cart = Cart.get_instance().get_products()
    # cart_total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, cart_total=Cart.get_instance().get_total())

if __name__ == "__main__":
    app.run(debug=True)

