#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from api.off import OFF
from views.product_view import ProductView


class ProductController:

    def __init__(self):
        pass

    @staticmethod
    def api_get(category, page_size):
        api = OFF()
        return api.get_products(category, page_size)

    @staticmethod
    def get(category):
        database = Database()
        return database.get_products(category)

    @staticmethod
    def set(products):
        database = Database()
        database.set_products(products)

    @staticmethod
    def get_substitutes(product, max_products):
        database = Database()
        return database.get_substitutes(product, max_products)

    @staticmethod
    def display_product(product):
        product_view = ProductView()
        product_view.display_product(product)

    @staticmethod
    def display_products(products):
        product_view = ProductView()
        return product_view.display_products(products)

    @staticmethod
    def display_list(products):
        product_view = ProductView()
        return product_view.display_list(products)

    @staticmethod
    def display_substitute(product, substitute):
        product_view = ProductView()
        return product_view.display_substitute(product, substitute)

    @staticmethod
    def select(prompt, products):
        product = ''
        while product == '' or product not in products:
            product = input(prompt)
        return product
