#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import mysql.connector as database

from app.category import Category


class Database:

    def __init__(self, connection_config):
        self.connection_config = connection_config

    def set_categories(self, categories):
        with database.connect(**self.connection_config) as connection:
            for category in categories:
                with connection.cursor() as cursor:
                    query = ("SELECT category_id from Category WHERE name = %s")
                    cursor.execute(query, (category.name, ))
                    if not cursor.fetchone():
                        query = ("INSERT INTO Category (name) VALUES (%s)")
                        cursor.execute(query, (category.name, ))
            connection.commit()

    def get_categories(self):
        categories = []
        with database.connect(**self.connection_config) as connection:
            with connection.cursor() as cursor:
                query = ("SELECT category_id, name from Category")
                cursor.execute(query)
                for category_id, name in cursor:
                    categories.append(Category(category_id, name))
            connection.commit()
        return categories
