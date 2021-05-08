#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.product_view import ProductView


class SubstituteView:

    def __init__(self):
        self.product_view = ProductView()

    def display_substitute(self, product, substitute, category):
        print()
        print("Aliment substitué :")
        self.product_view.display_product(product, category)
        print("Aliment de substitution :")
        self.product_view.display_product(substitute, category)
        prompt = "Enregistrer dans mes aliments substitués ? : "
        return prompt
