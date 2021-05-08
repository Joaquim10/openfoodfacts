#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from views.substitute_view import SubstituteView


class SubstituteController:

    def __init__(self):
        self.database = Database()

    def set_substitute(self, product, substitute):
        self.database.set_substitute(product, substitute)

    @staticmethod
    def display_substitute(product, substitute, category):
        substitute_view = SubstituteView()
        return substitute_view.display_substitute(
                                        product, substitute, category)

    def display_substitutes(self):
        substitutes = self.database.get_substitutes()
        for substitution in substitutes:
            product = self.database.get_product(substitution)
            substitute = self.database.get_substitute(substitution)
            category = self.database.get_category(substitution)
            self.display_substitute(product, substitute, category)
