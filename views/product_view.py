#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class ProductView:

    def __init__(self):
        pass

    @staticmethod
    def display_product(product, category):
        print("Numéro      : {}".format(product.product_id))
        print("Nom         : {}".format(product.name))
        print("Catégorie   : {}".format(category.name))
        print("Description : {}".format(product.description))
        print("Nutri-score : {}".format(product.nutri_score.upper()))
        magasins = ', '.join(product.stores.split(','))
        print("Magasins    : {}".format(magasins))
        print("Lien        : {}".format(product.url))

    @staticmethod
    def display_products(products):
        prompt = "Selectionnez un aliment : "
        for product in products:
            print("{} - {} [{}]".format(product.product_id, product.name,
                                        product.nutri_score.upper()))
        return prompt

    def display_healthy_products(self, products, category):
        prompt = "Selectionnez un aliment de substitution : "
        for product in products:
            print()
            self.display_product(product, category)
        return prompt

    def display_substitute(self, product, substitute, category):
        print()
        print("--- Aliment substitué ---")
        self.display_product(product, category)
        print("--- Aliment de substitution ---")
        self.display_product(substitute, category)

    def display_selected_substitute(self, product, substitute, category):
        prompt = "Enregistrer dans mes aliments substitués ? : "
        self.display_substitute(product, substitute, category)
        return prompt

    def display_selected_product(self, product, category):
        print()
        print("--- Aliment sélectionné ---")
        self.display_product(product, category)
        print("--- Aucun aliment de substitution trouvé ! ---")
