#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

product_controler: product_controler contains the ProductController class.

Classes:
    ProductController: The ProductController object processes the product
    controller.

Methods:
    get_products(self, categories):
        Gets the products of the specified categories from the
        Open Food Facts API.
    set_products(products):
        Sets the products to database.
    select_product(category):
        Gets a product of the specified category from the product menu.
    select_substitute(product, category):
        Gets a substitute for a product from the substitute menu.
"""

from database.database import Database
from api.off import OFF
from models.product import Product
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

    @staticmethod
    def _get_product(category, json_product):
        '''Gets a cleaned product from a product in json format.'''
        product = {
            'product_id': None,
            'name': None,
            'category_id': category.category_id,
            'description': '',
            'nutri_score': None,
            'stores': '',
            'url': None
        }
        product = Product(product)
        if 'product_name_fr' in json_product:
            if json_product['product_name_fr'] != '':
                product.name = json_product['product_name_fr']
        elif 'product_name' in json_product:
            if json_product['product_name'] != '':
                product.name = json_product['product_name']
        if 'generic_name_fr' in json_product:
            product.description = json_product['generic_name_fr']
        elif 'generic_name' in json_product:
            product.description = json_product['generic_name']
        if 'nutrition_grade_fr' in json_product:
            if json_product['nutrition_grade_fr'] in 'abcdeABCDE':
                product.nutri_score = json_product['nutrition_grade_fr']
        if 'stores' in json_product:
            product.stores = json_product['stores']
        if 'url' in json_product:
            url = json_product['url'].lower()
            if 'https://' in url and '.openfoodfacts.org/' in url:
                product.url = json_product['url']
        if not (product.name and product.nutri_score and product.url):
            product = None
        return product

    def get_products(self, categories):
        '''

        Gets the products of the specified categories from the
        Open Food Facts API.

        This method gets the products of the specified categories from the
        Open Food Facts API in a json format, then extracts the
        products from the json format, checks their integrity and returns the
        cleaned products.

            Args:
                categories (category.Category): The categories.

            Returns:
                products (list [product.Product]): The products.
        '''

        api = OFF()
        products = []
        for category in categories:
            json_products = api.get_products(category)
            for json_product in json_products:
                product = self._get_product(category, json_product)
                if product:
                    products.append(product)
        return products

    def set_products(self, products):
        '''

        Sets the products to database.

            Args:
                products (list [product.Products]): The products.
        '''
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
        product = None
        if products:
            prompt = self.product_view.display_products(products)
            product = self._select_product(prompt, products)
        return product

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
        products = self.database.get_healthy_products(product)
        product = None
        if products:
            prompt = self.product_view.display_healthy_products(products,
                                                                category)
            product = self._select_product(prompt, products)
        return product
