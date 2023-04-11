from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

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

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products (name, price, product_profile_image, quantity) VALUES (%s, %s, %s, %s)",
                (name, price, profile, quantity))
    mysql.connection.commit()
    cur.close()

    data = {'message': 'Saved successfuly'}
    return jsonify(data)


@app.route('/api/products')
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products ORDER BY id DESC")
    results = cur.fetchall()
    cur.close()
    products_list = []
    for row in results:
        product = {'id': row[0], 'name': row[1],
                   'price': row[2], 'profile': row[3], 'quantity': row[4]}
        products_list.append(product)
    return jsonify(products_list)


@app.route('/api/search', methods=['POST'])
def search():
    querry = request.form['querry']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE name LIKE '%" +
                querry + "%' ORDER BY id DESC")

    results = cur.fetchall()
    cur.close()
    products_list = []
    for row in results:
        product = {'id': row[0], 'name': row[1],
                   'price': row[2], 'profile': row[3], 'quantity': row[4]}
        products_list.append(product)
    return jsonify(products_list)


if __name__ == "__main__":
    app.run(debug=True)
