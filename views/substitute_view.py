#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

substitute_view: substitute_view contains the SubstituteView class.

Classes:
    SubstituteView: The SubstituteView object processes the substitute view.

Methods:
    display_substitute(product, substitute, category):
        Displays the specified substitute and its substitueted product with
        its category.
"""

from views.product_view import ProductView


class SubstituteView:
    """

    The SubstituteView object initializes and processes the substituteview.

    Attributes:
        product_view (product_view.ProductView): The product view.
    """
    def __init__(self):
        self.product_view = ProductView()

    def display_substitute(self, product, substitute, category):
        '''
        Displays the specified substitute and its substitueted product with
        its category.

        Args:
            product (product.Product): The product.
            substitute (product.Product): The substitute.
            category (category.Category): The category.

        Returns:
            prompt (str): The prompt.
        '''
        print()
        print("Aliment substitué :")
        self.product_view.display_product(product, category)
        print("Aliment de substitution :")
        self.product_view.display_product(substitute, category)
        prompt = "Enregistrer dans mes aliments substitués ? : "
        return prompt
