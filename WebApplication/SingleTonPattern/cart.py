class Cart:
    __instance = None

    def __init__(self, mysql):
        Cart.__instance = self
        self.mysql = mysql
        self.products = []

    @staticmethod
    def get_instance():
        if Cart.__instance is None:
            Cart()
        return Cart.__instance

    def product_details(self, id,quantity):
        query = "SELECT name,unit_price FROM products WHERE id = %s"
        cur = self.mysql.connection.cursor()
        cur.execute(query, (id,))
        result = cur.fetchone()

        if result is not None:
            name = result[0]
            price = result[1]
            return {'id': id, 'name':name, 'price':price,'quantity':quantity}

    def add_product(self,product):
        cur = self.mysql.connection.cursor()

        cur.execute("INSERT INTO cart (product_id,quantity) VALUES (%s, %s)",
                    (product['id'],product['quantity']))
        
        self.mysql.connection.commit()
        cur.close()
        
        self.products.append(product)

    def remove_product(self, product):
        cur = self.mysql.connection.cursor()

        cur.execute("DELETE FROM cart WHERE product_id = %s", (int(product['id']),))

        # Commit the transaction
        self.mysql.connection.commit()

        # Close the cursor
        cur.close()

        self.products.remove(product)

    def get_products(self):
        return self.products
    
    def checkout(self):
        cur = self.mysql.connection.cursor()
        for i in self.products:
            id = i['id']
            price = i['price']
            quantity = i['quantity']
            item_total = price * int(quantity)

            cur.execute("INSERT INTO sales (product_id,quantity,amount_paid) VALUES (%s, %s,%s)",
                    (id,int(quantity),int(item_total)))
            
            self.remove_product(i)
        
            self.mysql.connection.commit()
        
        cur.close()
        self.clear_cart()

    def clear_cart(self):
        self.products = []

    def get_total(self):
        total = 0.0
        for i in self.products:
            price = i['price']
            quantity = i['quantity']
            item_total = price * int(quantity)
            total += item_total

        return total
