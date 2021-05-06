#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import mysql.connector as connector
import config.db_config as db_config
from models.category import Category
from models.product import Product
from models.substitute import Substitute


class Database:

    def __init__(self):
        self.connection_config = db_config.CONNECTION

    def reset_tables(self):
        directory = os.path.dirname(__file__)
        sql_file = os.path.join(directory, 'openfoodfacts.sql')
        password = '--password'
        if self.connection_config['password'] != '':
            password = [password, self.connection_config['password']]
            password = '='.join(password)
        command = [
            'mysql --host=', self.connection_config['host'],
            ' --port=', self.connection_config['port'],
            ' --user=', self.connection_config['user'],
            ' ', password,
            ' < ', sql_file
        ]
        command = ''.join(command)
        os.system(command)

    def get_categories(self):
        categories = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT category_id, name "
                         "FROM Category "
                         "ORDER BY category_id ASC")
                cursor.execute(query)
                for category_id, name in cursor:
                    categories.append(Category(category_id, name))
            connection.commit()
        return categories

    def set_categories(self, categories):
        with connector.connect(**self.connection_config) as connection:
            for category_name in categories:
                category = Category(None, category_name)
                with connection.cursor() as cursor:
                    query = ("SELECT category_id "
                             "FROM Category "
                             "WHERE name = %s")
                    data = (category.name, )
                    cursor.execute(query, data)
                    if not cursor.fetchall():
                        query = ("INSERT INTO Category (name) "
                                 "VALUES (%s)")
                        cursor.execute(query, data)
            connection.commit()

    def get_category(self, category_id):
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT category_id, name "
                         "FROM Category "
                         "WHERE category_id = %s")
                data = (category_id, )
                cursor.execute(query, data)
                category_id, name = cursor.fetchone()
                category = Category(category_id, name)
            connection.commit()
        return category

    def get_products(self, category):
        products = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT product_id, name, category_id, "
                         "description, nutri_score, stores, url "
                         "FROM Product "
                         "WHERE category_id = %s "
                         "ORDER BY product_id ASC")
                data = (category.category_id, )
                cursor.execute(query, data)
                for product_id, name, category_id, description, \
                        nutri_score, stores, url in cursor:
                    product = {
                        'product_id': product_id,
                        'name': name,
                        'category_id': category_id,
                        'description': description,
                        'nutri_score': nutri_score,
                        'stores': stores,
                        'url': url
                    }
                    products.append(Product(product))
            connection.commit()
        return products

    def set_products(self, products):
        with connector.connect(**self.connection_config) as connection:
            for product in products:
                with connection.cursor() as cursor:
                    query = ("INSERT INTO Product "
                             "(name, category_id, description, "
                             "nutri_score, stores, url) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")
                    data = [
                        product.name,
                        product.category_id,
                        product.description,
                        product.nutri_score,
                        product.stores,
                        product.url
                    ]
                    cursor.execute(query, data)
            connection.commit()

    def get_product(self, product_id):
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT product_id, name, category_id, "
                         "description, nutri_score, stores, url "
                         "FROM Product "
                         "WHERE product_id = %s")
                data = (product_id, )
                cursor.execute(query, data)
                product_id, name, category_id, description, nutri_score, \
                    stores, url = cursor.fetchone()
                product = {
                    'product_id': product_id,
                    'name': name,
                    'category_id': category_id,
                    'description': description,
                    'nutri_score': nutri_score,
                    'stores': stores,
                    'url': url
                }
                product = Product(product)
            connection.commit()
        return product

    def get_healthy_products(self, product, max_products):
        products = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT product_id, name, category_id, "
                         "description, nutri_score, stores, url "
                         "FROM Product "
                         "WHERE category_id = %s AND nutri_score < %s"
                         "ORDER BY nutri_score ASC "
                         "LIMIT %s OFFSET 0")
                data = [product.category_id, product.nutri_score, max_products]
                cursor.execute(query, data)
                for product_id, name, category_id, description, \
                        nutri_score, stores, url in cursor:
                    product = {
                        'product_id': product_id,
                        'name': name,
                        'category_id': category_id,
                        'description': description,
                        'nutri_score': nutri_score,
                        'stores': stores,
                        'url': url
                    }
                    products.append(Product(product))
            connection.commit()
        return products

    def get_substitutes(self):
        substitutes = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT product_id, substitute_id "
                         "FROM Substitute "
                         "ORDER BY product_id ASC, substitute_id ASC")
                cursor.execute(query)
                for product_id, substitute_id in cursor:
                    substitutes.append(Substitute(product_id, substitute_id))
            connection.commit()
        return substitutes

    def set_substitute(self, substitute):
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT substitute_id "
                         "FROM Substitute "
                         "WHERE product_id = %s AND substitute_id = %s")
                data = [substitute.product_id, substitute.substitute_id]
                cursor.execute(query, data)
                if not cursor.fetchall():
                    query = ("INSERT INTO Substitute "
                             "(product_id, substitute_id) "
                             "VALUES (%s, %s)")
                    cursor.execute(query, data)
            connection.commit()
