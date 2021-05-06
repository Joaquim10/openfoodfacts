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

    def get_product(self, product_id):
        return self.database.get_product(product_id)

    def get_healthy_products(self, product, max_products):
        return self.database.get_healthy_products(product, max_products)

    def display_products(self, products):
        return self.product_view.display_products(products)

    def display_healthy_products(self, products, category):
        return self.product_view.display_healthy_products(products, category)

    def display_selected_substitute(self, product, substitute, category):
        return self.product_view.display_substitute(
                                        product, substitute, category)

    def display_selected_product(self, product, category):
        self.product_view.display_selected_product(product, category)

    def display_substitute(self, product, substitute, category):
        self.product_view.display_substitute(product, substitute, category)

    @staticmethod
    def select(prompt, products):
        product = ''
        while product not in products or product == '':
            product = input(prompt)
        return product
