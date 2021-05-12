#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

product_controler: product_controler contains the ProductController class.

Classes:
    ProductController: The ProductController object processes the product
    controller.

Methods:
    set_products(categories):
        Sets the products of the specified categories to database.
    select_product(category):
        Gets a product of the specified category from the product menu.
    select_substitute(product, category):
        Gets a substitute for a product from the substitute menu.
"""

import config.settings as settings
from database.database import Database
from api.off import OFF
from views.product_view import ProductView


class ProductController:
    """

    The ProductController object initializes and processes the product
    controller.

    Attributes:
        database (database.Database): The database.
        product_view (product_view.ProductView): The product view.
    """
    def __init__(self):
        self.database = Database()
        self.product_view = ProductView()

    def set_products(self, categories):
        '''

        Sets the products of the specified categories to database.

        This method gets a page of products from the specified categories from
        the Open Food Facts API and sets them to the database.

            Args:
                categories (list [category.Category]): The categories.
        '''
        api = OFF()
        products = []
        for category in categories:
            api_products = api.get_products(category, settings.MAX_PRODUCTS)
            products.extend(api_products)
        self.database.set_products(products)

    @staticmethod
    def _select_product(prompt, products):
        '''Asks the user for a product.'''
        selected_product = None
        while not selected_product:
            option = input(prompt)
            for product in products:
                if option == str(product.product_id):
                    selected_product = product
                    break
        return selected_product

    def select_product(self, category):
        '''

        Gets a product of the specified category from the product menu.

        This method gets all the products of the specified category from the
        database, then displays a menu of these products and asks the user for
        a product and finally returns the selected product.

            Args:
                category (category.Category): The category.

            Returns:
                product (product.Product): The selected product.
        '''
        products = self.database.get_products(category)
        prompt = self.product_view.display_products(products)
        return self._select_product(prompt, products)

    def select_substitute(self, product, category):
        '''

        Gets a substitute for a product from the substitute menu.

        This method gets some potential substitutes for the product from the
        database, then displays a menu of these products with their categories
        and asks the user for a substitute and finally returns the selected
        substitute.

            Args:
                product (product.Product): The product.
                category (category.Category): The category.

            Returns:
                substitute (product.Product): The selected substitute.
        '''
        products = self.database.get_healthy_products(product,
                                                      settings.MAX_SUBSTITUTES)
        prompt = self.product_view.display_healthy_products(products, category)
        return self._select_product(prompt, products)
