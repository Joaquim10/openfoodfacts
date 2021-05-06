#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.substitute_controller import SubstituteController
from controllers.menu_controller import MenuController
from controllers.message_controller import MessageController
from database.database import Database
from models.substitute import Substitute


class OpenFoodFacts:

    def __init__(self):
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.substitute_controller = SubstituteController()
        self.run()

    def get_categories(self):
        return self.category_controller.get()

    def set_categories(self, categories):
        self.category_controller.set(categories)

    def get_products(self, category):
        return self.product_controller.get(category)

    def get_category(self, category_id):
        return self.category_controller.get_category(category_id)

    def set_products(self):
        products = []
        categories = self.get_categories()
        for category in categories:
            api_products = self.product_controller.api_get(
                            category, settings.MAX_PRODUCTS)
            for product in api_products:
                products.append(product)
        self.product_controller.set(products)

    def reset_database(self):
        database = Database()
        database.reset_tables()
        self.set_categories(settings.CATEGORIES)
        self.set_products()

    def get_product(self, product_id):
        return self.product_controller.get_product(product_id)

    def get_healthy_products(self, product):
        return self.product_controller.get_healthy_products(
                                            product, settings.MAX_SUBSTITUTES)

    def get_substitutes(self):
        return self.substitute_controller.get()

    def set_substitute(self, product, substitute):
        self.substitute_controller.set(
            Substitute(product.product_id, substitute.product_id))

    def select_category(self):
        selected_category = None
        options = []
        categories = self.get_categories()
        prompt = self.category_controller.display(categories)
        for category in categories:
            options.append(str(category.category_id))
        category_id = int(self.category_controller.select(prompt, options))
        for category in categories:
            if category_id == category.category_id:
                selected_category = category
                break
        return selected_category

    def select(self, products, prompt):
        selected_product = None
        options = []
        for product in products:
            options.append(str(product.product_id))
        product_id = int(self.product_controller.select(prompt, options))
        for product in products:
            if product_id == product.product_id:
                selected_product = product
                break
        return selected_product

    def select_product(self, category):
        products = self.get_products(category)
        prompt = self.product_controller.display_products(products)
        return self.select(products, prompt)

    def select_substitute(self, product, category):
        selected_product = None
        products = self.get_healthy_products(product)
        if products:
            prompt = self.product_controller.display_healthy_products(
                                                        products, category)
            selected_product = self.select(products, prompt)
        return selected_product

    def display_selected_substitute(self, product, substitute, category):
        self.product_controller.display_selected_substitute(
                                        product, substitute, category)

    def display_selected_product(self, product, category):
        self.product_controller.display_selected_product(product, category)

    def display_substitutes(self):
        substitutes = self.get_substitutes()
        for substitution in substitutes:
            product = self.get_product(substitution.product_id)
            substitute = self.get_product(substitution.substitute_id)
            category = self.get_category(substitute.category_id)
            self.product_controller.display_substitute(
                                                product, substitute, category)

    def run(self):
        menu_controller = MenuController()
        message_controller = MessageController()
        option = ''
        while option != '0':
            prompt = menu_controller.display_main_menu()
            option = menu_controller.select(prompt, '1290')
            if option == '1':
                category = self.select_category()
                product = self.select_product(category)
                substitute = self.select_substitute(product, category)
                if substitute:
                    self.display_selected_substitute(
                                                product, substitute, category)
                    prompt = menu_controller.display_save_menu()
                    option = menu_controller.select(prompt, '10')
                    if option == '1':
                        self.set_substitute(product, substitute)
                    option = ''
                else:
                    self.display_selected_product(product, category)
            elif option == '2':
                self.display_substitutes()
            elif option == '9':
                message_controller.database_reset()
                self.reset_database()
