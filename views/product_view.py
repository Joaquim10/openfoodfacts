#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class ProductView:

    def __init__(self):
        pass

    @staticmethod
    def display_products(products):
        print()
        for product in products:
            print("{} - {}".format(product.product_id, product.name))
        prompt = "Selectionnez un aliment : "
        return prompt

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

    def display_healthy_products(self, products, category):
        for product in products:
            print()
            self.display_product(product, category)
        prompt = "Selectionnez un aliment de substitution : "
        return prompt
