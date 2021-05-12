#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

database: database contains the Database class.

Classes:
    Database: The Database object processes the database.

Methods:
    reset_tables():
        Resets the tables of the database.
    get_categories():
        Gets all the categories.
    set_categories(categories):
        Sets the specified categories.
    get_products(category):
        Gets all the products of the specified category.
    set_products(products):
        Sets the specified products.
    get_healthy_products(product, max_products):
        Gets some potential substitutes for the product.
    get_substitutes():
        Gets all the substitutes.
    set_substitute(product, substitute):
        Sets the substitute.
    get_product(substitute):
        Gets the substitued product from the substitute.
    get_substitute(substitute):
        Gets the product of substitution from the substitute.
    get_category(substitute):
        Gets the category from the substitute.
"""

import os
import mysql.connector as connector
import config.db_config as db_config
from models.category import Category
from models.product import Product
from models.substitute import Substitute


class Database:
    """

    The Database object initializes and processes the database.

    Attributes:
        connection_config: The connection configuration.
    """
    def __init__(self):
        self.connection_config = db_config.CONNECTION

    def reset_tables(self):
        '''Resets the tables of the database.'''
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
        '''

        Gets all the categories.

        Returns:
            categories (list [category.Category]): The categories.
        '''
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
        '''
        Sets the specified categories.

        Args:
            categories (list [category.Category]): The categories.
        '''
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

    def get_products(self, category):
        '''

        Gets all the products of the specified category.

        Args:
            category (category.Category): The category.

        Returns:
            products (list [product.Product]): Products.
        '''
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
        '''

        Sets the specified products.

        Args:
            products (list [product.Product]): The products.
        '''
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

    def get_healthy_products(self, product, max_products):
        '''

        Gets some potential substitutes for the specified product.

            Args:
                product (product.Product): The product.
                max_products (int): Maximum number of products.

            Returns:
                products (list [product.Product]): The potential substitutes.
        '''
        products = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT product_id, name, category_id, "
                         "description, nutri_score, stores, url "
                         "FROM Product "
                         "WHERE category_id = %s AND nutri_score <= %s "
                         "AND product_id != %s "
                         "ORDER BY nutri_score ASC "
                         "LIMIT %s OFFSET 0")
                data = [product.category_id, product.nutri_score,
                        product.product_id, max_products]
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
        '''

        Gets all the substitutes.

        Returns:
            substitutes (list [substitute.Substitute]): The substitutes.
        '''
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

    def set_substitute(self, product, substitute):
        '''

        Sets the substitute.

        Args:
            product (product.Product): The product.
            substitute (product.Product): The substitute.
        '''
        substitute = Substitute(product.product_id, substitute.product_id)
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

    def _get_product(self, product_id):
        '''Gets the product with the specified product id.'''
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

    def get_product(self, substitute):
        '''

        Gets the substitued product from the substitute.

        Args:
            substitute (substitute.Substitute): The substitute.

        Returns:
            product (product.Product): The product.
        '''
        return self._get_product(substitute.product_id)

    def get_substitute(self, substitute):
        '''

        Gets the product of substitution from the substitute.

        Args:
            substitute (substitute.Substitute): The substitute.

        Returns:
            product (product.Product): The product of substitution.
        '''

        return self._get_product(substitute.substitute_id)

    def get_category(self, substitute):
        '''

        Gets the category from the substitute.

        Args:
            substitute (substitute.Substitute): The substitute.

        Returns:
            category (category.Category): The category.
        '''
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT Category.category_id, Category.name "
                         "FROM Substitute "
                         "INNER JOIN Product "
                         "ON Substitute.substitute_id = Product.product_id "
                         "INNER JOIN Category "
                         "ON Product.category_id = Category.category_id "
                         "WHERE Substitute.substitute_id = %s")
                data = (substitute.substitute_id, )
                cursor.execute(query, data)
                category_id, name = cursor.fetchone()
                category = Category(category_id, name)
            connection.commit()
        return category
