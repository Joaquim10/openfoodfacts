#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from models.category import Category
from models.product import Product
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController


class OpenFoodFacts:

    def __init__(self):
        self.categories = self.init_categories(settings.CATEGORIES)

    def init_categories(self, category_names):
        categories = []
        category_controller = CategoryController()
        for category in category_names:
            categories.append(Category(category))
        category_controller.set(categories)
        return category_controller.get()

    def run(self):
        product_controller = ProductController()
        for category in self.categories:
            print(category.category_id, category.name, '...')
            products = product_controller.api_get_products(
                category, settings.MAX_PRODUCTS)
            print(products[0])
