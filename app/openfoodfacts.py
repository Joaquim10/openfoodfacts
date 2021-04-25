#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.menu_controller import MenuController


class OpenFoodFacts:

    def __init__(self):
        pass

    @staticmethod
    def get_categories():
        category_controller = CategoryController()
        return category_controller.get()

    @staticmethod
    def set_categories(categories):
        category_controller = CategoryController()
        category_controller.set(categories)

    def set_products(self, categories):
        products = []
        product_controller = ProductController()
        categories = self.get_categories()
        for category in categories:
            api_products = (product_controller.api_get(
                category, settings.MAX_PRODUCTS))
            for product in api_products:
                products.append(product)
        product_controller.set(products)

    def db_reset(self):
        self.set_categories(settings.CATEGORIES)
        self.set_products(self.get_categories())

    def run(self):
        menu_controller = MenuController()
        menu_controller.title()
        prompt = menu_controller.main_menu()
        command = ''
        while command != '0':
            command = menu_controller.prompt(prompt)