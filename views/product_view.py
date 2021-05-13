#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

product_view: product_view contains the ProductView class.

Classes:
    ProductView: The ProductView object processes the product view.

Methods:
    display_products(products):
        Displays the specified products and returns the prompt.
    display_product(product, category):
        Displays the specified product with their category.
    display_healthy_products(self, products, category):
        Displays the specified products with their category and returns the
        prompt.
"""


class ProductView:
    """The ProductView object initializes and processes the product view."""
    def __init__(self):
        pass

    @staticmethod
    def display_products(products):
        '''
        Displays the specified products and returns the prompt.

        Args:
            product (list [product.Product]): The products.

        Returns:
            prompt (str): The prompt.
        '''
        print()
        for product in products:
            print("{} - {}".format(product.product_id, product.name))
        prompt = "Selectionnez un aliment : "
        return prompt

    @staticmethod
    def display_product(product, category):
        '''
        Displays the specified product with their category.

        Args:
            product (product.Product): The product.
            category (category.Category): The category.
        '''
        print("Numéro      : {}".format(product.product_id))
        print("Nom         : {}".format(product.name))
        print("Catégorie   : {}".format(category.name))
        print("Description : {}".format(product.description))
        print("Nutri-score : {}".format(product.nutri_score.upper()))
        magasins = ', '.join(product.stores.split(','))
        print("Magasins    : {}".format(magasins))
        print("Lien        : {}".format(product.url))

    def display_healthy_products(self, products, category):
        '''
        Displays the specified products with their category and returns the
        prompt.

        Args:
            products (list [product.Product]): The products.
            category (category.Category): The category.

        Returns:
            prompt (str): The prompt.
        '''
        for product in products:
            print()
            self.display_product(product, category)
        prompt = "Selectionnez un aliment de substitution : "
        return prompt
