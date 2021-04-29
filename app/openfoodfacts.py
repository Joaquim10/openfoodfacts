#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.menu_controller import MenuController
from controllers.message_controller import MessageController
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

    def set_products(self):
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
        self.set_products()

    def run(self):
        message_controller = MessageController()
        menu_controller = MenuController()
        prompt = menu_controller.main_menu()
        keys = '1290'
        key = ''
        while key != '0':
            key = menu_controller.prompt(prompt, keys)
            if key == '9':
                message = 'Réinitialisation de la base de données en cours...'
                message_controller.message(message)
                self.reset_database()
            message_controller.message('')
            prompt = menu_controller.main_menu()
