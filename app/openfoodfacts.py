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

    @staticmethod
    def get_products(category):
        product_controller = ProductController()
        return product_controller.get(category)

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

    @staticmethod
    def get_substitutes(product):
        product_controller = ProductController()
        return product_controller.get_substitutes(
            product, settings.MAX_SUBSTITUTES)

    def reset_database(self):
        database = Database()
        database.reset_tables()
        self.set_categories(settings.CATEGORIES)
        self.set_products()

    def select_category(self):
        selected_category = None
        commands = []
        category_controller = CategoryController()
        categories = self.get_categories()
        prompt = category_controller.display(categories)
        for category in categories:
            commands.append(str(category.category_id))
        category_id = int(category_controller.select(prompt, commands))
        for category in categories:
            if category_id == category.category_id:
                selected_category = category
                break
        return selected_category

    def select_product(self, category):
        selected_product = None
        commands = []
        product_controller = ProductController()
        products = self.get_products(category)
        prompt = product_controller.display_list(products)
        for product in products:
            commands.append(str(product.product_id))
        product_id = int(product_controller.select(prompt, commands))
        for product in products:
            if product_id == product.product_id:
                selected_product = product
                break
        return selected_product

    def select_substitute(self, product):
        selected_product = None
        commands = []
        product_controller = ProductController()
        products = self.get_substitutes(product)
        if products:
            prompt = product_controller.display_products(products)
            for substitute in products:
                commands.append(str(substitute.product_id))
            product_id = int(product_controller.select(prompt, commands))
            for substitute in products:
                if product_id == substitute.product_id:
                    selected_product = substitute
                    break
        return selected_product

    @staticmethod
    def display_substitute(product, substitute):
        product_controller = ProductController()
        product_controller.display_substitute(product, substitute)

    @staticmethod
    def display(product):
        product_controller = ProductController()
        product_controller.display_product(product)

    def run(self):
        menu_controller = MenuController()
        message_controller = MessageController()
        key = ''
        while key != '0':
            prompt = menu_controller.display()
            keys = '1290'
            key = menu_controller.select(prompt, keys)
            if key == '1':
                category = self.select_category()
                product = self.select_product(category)
                substitute = self.select_substitute(product)
                self.display_substitute(product, substitute)
            elif key == '2':
                pass
            elif key == '9':
                message = 'Réinitialisation de la base de données en cours...'
                message_controller.message(message)
                self.reset_database()
            message_controller.message('')
