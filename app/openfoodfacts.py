#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

openfoodfacts: openfoodfacts contains the OpenFoodFacts class.

Classes:
    OpenFoodFacts: The OpenFoodFacts object runs the application.

Methods:
    replace_product(): Replace a product by a substitute.
    display_substitutes(): Display all the subtitutes and their substitued
        products.
    reset_database(): Resets the database.
    run(): Runs the application.
"""

from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.substitute_controller import SubstituteController
from controllers.menu_controller import MenuController
from controllers.message_controller import MessageController
from database.database import Database


class OpenFoodFacts:
    """

    The OpenFoodFacts object initializes and runs the application.

    Attributes:
        menu_controller (menu_controller.MenuController):
            The menu controller.
        category_controller (category_controller.CategoryController):
            The category controller.
        product_controller (product_controller.ProductController):
            The product controller.
        substitute_controller (substitute_controller.SubstituteController):
            The substitute controller.
        message_controller(message_controller)
            The message controller.
    """
    def __init__(self):
        self.menu_controller = MenuController()
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.substitute_controller = SubstituteController()
        self.message_controller = MessageController()
        self.run()

    def replace_product(self):
        '''

        Replace a product by a substitute.

        This method processes the replacement of a product by a substitute.
        The user chooses a category, a product from the selected catagory
        and a substitute for this product. A save menu is then displayed and
        the user can choose to save the substitute. Finally, the substitute is
        saved if the user has choosen to do so.
        If there is no product or substitute selected, this method ends.
        '''
        category = self.category_controller.select_category()
        product = self.product_controller.select_product(category)
        if product:
            substitute = self.product_controller.select_substitute(product,
                                                                   category)
            if substitute:
                self.substitute_controller.display_substitute(
                                                product, substitute, category)
                option = self.menu_controller.select_save_option()
                if option != 0:
                    self.substitute_controller.set_substitute(product,
                                                              substitute)

    def display_substitutes(self):
        '''Displays all the subtitutes and their substitued products.'''
        self.substitute_controller.display_substitutes()

    def reset_database(self):
        '''

        Resets the database.

        This method displays a database reset message, resets the tables of
        the database and adds the categories and products to the database.
        '''
        database = Database()
        self.message_controller.display_database_reset_message()
        database.reset_tables()
        self.category_controller.set_categories()
        categories = self.category_controller.get_categories()
        products = self.product_controller.get_products(categories)
        self.product_controller.set_products(products)

    def run(self):
        '''

        Runs the application.

        This method processes the main menu.
        The user can choose to replace a product by a substitute, display all
        the substitutes and their substitued products, reset the database and
        exit the application.
        '''
        option = -1
        while option != 0:
            option = self.menu_controller.select_main_option()
            if option == 1:
                self.replace_product()
            elif option == 2:
                self.display_substitutes()
            elif option == 9:
                self.reset_database()
