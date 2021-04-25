#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import mysql.connector as connector

import config.db_config as db_config
from models.category import Category


class Database:

    def __init__(self):
        self.connection_config = db_config.CONNECTION

    def get_categories(self):
        categories = []
        with connector.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT category_id, name from Category")
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
                    query = ("SELECT category_id FROM Category "
                             "WHERE name = %s")
                    data = (category.name, )
                    cursor.execute(query, data)
                    if not cursor.fetchall():
                        query = ("INSERT INTO Category (name) VALUES (%s)")
                        cursor.execute(query, data)
            connection.commit()

    def set_products(self, products):
        with connector.connect(**self.connection_config) as connection:
            for product in products:
                with connection.cursor() as cursor:
                    query = ("SELECT product_id FROM Product WHERE name = %s")
                    data = (product.name, )
                    cursor.execute(query, data)
                    if not cursor.fetchall():
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
