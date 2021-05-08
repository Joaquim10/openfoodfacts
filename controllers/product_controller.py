#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from database.database import Database
from api.off import OFF
from views.product_view import ProductView


class ProductController:

    def __init__(self):
        self.database = Database()
        self.product_view = ProductView()

    def set_products(self, categories):
        api = OFF()
        products = []
        for category in categories:
            api_products = api.get_products(category, settings.MAX_PRODUCTS)
            products.extend(api_products)
        self.database.set_products(products)

    @staticmethod
    def _select_product(prompt, products):
        selected_product = None
        while not selected_product:
            option = input(prompt)
            for product in products:
                if option == str(product.product_id):
                    selected_product = product
                    break
        return selected_product

    def select_product(self, category):
        products = self.database.get_products(category)
        prompt = self.product_view.display_products(products)
        return self._select_product(prompt, products)

    def select_substitute(self, product, category):
        products = self.database.get_healthy_products(product,
                                                      settings.MAX_SUBSTITUTES)
        prompt = self.product_view.display_healthy_products(products, category)
        return self._select_product(prompt, products)
