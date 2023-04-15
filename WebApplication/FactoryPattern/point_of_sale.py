from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

class PointOfSale:
    def __init__(self, product_factory):
        self.product_factory = product_factory
    
    def sell_product(self, name, price, *args):
        product = self.product_factory.create_product(name, price, *args)
        return product
