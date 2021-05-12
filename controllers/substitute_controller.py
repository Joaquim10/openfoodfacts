#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

substitute_controller: substitute_controller contains the SubstituteController
class.

Classes:
    SubstituteController: The SubstituteController object processes the
    substitute controller.

Methods:
    set_substitute(product, substitute):
        Sets the substitute to the database.
    display_substitute(product, substitute, category):
        Displays the product and its substitute.
    display_substitutes():
        Displays all the products and their substitutes.
"""

from database.database import Database
from views.substitute_view import SubstituteView


class SubstituteController:
    """

    The SubstituteController object initializes and processes the substitute
    controller.

    Attributes:
        database (database.Database): The database.
    """
    def __init__(self):
        self.database = Database()

    def set_substitute(self, product, substitute):
        '''

        Sets the substitute to the database.

            Args:
                product (product.Product): The substitued product.
                substitute (product.Product): The substitute.
        '''
        self.database.set_substitute(product, substitute)

    @staticmethod
    def display_substitute(product, substitute, category):
        '''

        Displays the product and its substitute.

            Args:
                product (product.Product): The substitued product.
                substitute (product.Product): The substitute.
                category (category.Category): The category.
        '''
        substitute_view = SubstituteView()
        return substitute_view.display_substitute(
                                        product, substitute, category)

    def display_substitutes(self):
        '''

        Displays all the products and their substitutes.

        This method gets all substitutes, their substitued products and their
        categories from database and displays these substitutes and substitued
        products with their categories.
        '''
        substitutes = self.database.get_substitutes()
        for substitution in substitutes:
            product = self.database.get_product(substitution)
            substitute = self.database.get_substitute(substitution)
            category = self.database.get_category(substitution)
            self.display_substitute(product, substitute, category)
