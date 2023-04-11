class Product:
    __instance = None
    
    def __init__(self,mysql):
        Product.__instance = self
        self.mysql = mysql

    @staticmethod
    def get_instance():
        if Product.__instance is None:
            Product()
        return Product.__instance

    def insert_product(self, name, price, profile, quantity):
        cur = self.mysql.connection.cursor()

        cur.execute("INSERT INTO products (name, price, product_profile_image, quantity) VALUES (%s, %s, %s, %s)",
                    (name, price, profile, quantity))
        self.mysql.connection.commit()
        cur.close()

    def get_products(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM products ORDER BY id DESC")
        results = cur.fetchall()
        cur.close()
        products_list = []
        product = {}
        for row in results:
            product = {'id': row[0], 'name': row[1],
                       'price': row[2], 'profile': row[3], 'quantity': row[4]}
        products_list.append(product)

        return products_list

    def find_products(self, querry):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM products WHERE name LIKE '%" +
                    querry + "%' ORDER BY id DESC")

        results = cur.fetchall()
        cur.close()
        products_list = []
        for row in results:
            product = {'id': row[0], 'name': row[1],
                       'price': row[2], 'profile': row[3], 'quantity': row[4]}
        products_list.append(product)

        return products_list
