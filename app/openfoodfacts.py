#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.substitute_controller import SubstituteController
from controllers.menu_controller import MenuController
from controllers.message_controller import MessageController
from database.database import Database


class OpenFoodFacts:

    def __init__(self):
        self.menu_controller = MenuController()
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.substitute_controller = SubstituteController()
        self.run()

    def replace_product(self):
        category = self.category_controller.select_category()
        product = self.product_controller.select_product(category)
        substitute = self.product_controller.select_substitute(
                                                            product, category)
        self.substitute_controller.display_substitute(
                                                product, substitute, category)
        option = self.menu_controller.select_save_option()
        if option == 1:
            self.substitute_controller.set_substitute(product, substitute)

    def display_substitutes(self):
        self.substitute_controller.display_substitutes()

    def reset_database(self):
        database = Database()
        message_controller = MessageController()
        message_controller.display_database_reset_message()
        database.reset_tables()
        categories = self.category_controller.get_categories()
        self.product_controller.set_products(categories)

    def run(self):
        option = -1
        while option != 0:
            option = self.menu_controller.select_main_option()
            if option == 1:
                self.replace_product()
            elif option == 2:
                self.display_substitutes()
            elif option == 9:
                self.reset_database()
