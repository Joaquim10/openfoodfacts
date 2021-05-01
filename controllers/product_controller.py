#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from api.off import OFF
from views.product_view import ProductView


class ProductController:

    def __init__(self):
        self.database = Database()
        self.product_view = ProductView()

    @staticmethod
    def api_get(category, page_size):
        api = OFF()
        return api.get_products(category, page_size)

    def get(self, category):
        return self.database.get_products(category)

    def set(self, products):
        self.database.set_products(products)

    def get_substitutes(self, product, max_products):
        return self.database.get_substitutes(product, max_products)

    def set_substitute(self, product, substitute):
        self.database.set_substitute(product, substitute)

    def display_list(self, products):
        return self.product_view.display_list(products)

    def display_products(self, products):
        return self.product_view.display_products(products)

    def display_substitute(self, product, substitute):
        return self.product_view.display_substitute(product, substitute)

    @staticmethod
    def select(prompt, products):
        product = ''
        while product not in products or product == '':
            product = input(prompt)
        return product
