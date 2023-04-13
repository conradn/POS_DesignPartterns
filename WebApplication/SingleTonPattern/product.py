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

    def insert_product(self, name, price, quantity):
        cur = self.mysql.connection.cursor()

        cur.execute("INSERT INTO products (name, unit_price, quantity) VALUES (%s, %s, %s)",
                    (name, price, quantity))
        self.mysql.connection.commit()
        cur.close()

    def edit_product(self, id,name, price, quantity):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE products SET name = %s, unit_price = %s, quantity = %s WHERE id = %s",
                (name, price, quantity, id))
        self.mysql.connection.commit()
        cur.close()
    

    def get_products(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM products ORDER BY id DESC")
        results = cur.fetchall()
        cur.close()
        products_list = []
        product = None
        for row in results:
            product = {'id': row[0], 'name': row[1],
                       'price': row[2],'quantity': row[3]}
            products_list.append(product)

        return products_list

    def delete_product(self,id):
        cur = self.mysql.connection.cursor()
        sql = "DELETE FROM products WHERE id = %s"
        val = (id,)
        cur.execute(sql, val)
        self.mysql.connection.commit()
        cur.close()
    
    def find_products(self, querry):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM products WHERE name LIKE '%" +
                    querry + "%' ORDER BY id DESC")

        results = cur.fetchall()
        cur.close()
        products_list = []
        product = None
        for row in results:
            product = {'id': row[0], 'name': row[1],
                       'price': row[2],'quantity': row[3]}
            products_list.append(product)

        return products_list
