#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController


class OpenFoodFacts:

    def __init__(self):
        self.categories = self.init_categories(settings.CATEGORIES)

    def init_categories(self, category_names):
        category_controller = CategoryController()
        category_controller.set(category_names)
        return category_controller.get()

    def run(self):

        for category in self.categories:
            product_controller = ProductController()
            print(category.category_id, category.name, '...')
            products = product_controller.api_get_products(
                category, settings.MAX_PRODUCTS)
            print(products[0])
