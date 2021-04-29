#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.menu_controller import MenuController
from database.database import Database


class OpenFoodFacts:

    def __init__(self):
        self.run()


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

    def reset_database(self):
        database = Database()
        database.reset_tables()
        self.set_categories(settings.CATEGORIES)
        self.set_products(self.get_categories())

    def run(self):
        menu_controller = MenuController()
        menu_controller.title()
        prompt = menu_controller.main_menu()
        command = ''
        while command != '0':
            command = menu_controller.prompt(prompt)
            if command == '9':
                self.reset_database()
                prompt = menu_controller.main_menu()
