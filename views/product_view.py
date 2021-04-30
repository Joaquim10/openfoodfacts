#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class ProductView:

    def __init__(self):
        pass

    @staticmethod
    def display_product(product):
        print('Numéro      : {}'.format(product.product_id))
        print('Nom         : {}'.format(product.name))
        print('Description : {}'.format(product.description))
        print('Nutri-score : {}'.format(product.nutri_score.upper()))
        magasins = ', '.join(product.stores.split(','))
        print('Magasins    : {}'.format(magasins))
        print('Lien        : {}'.format(product.url))

    @staticmethod
    def display_list(products):
        prompt = 'Selectionnez un aliment : '
        for product in products:
            print('{} - {} [{}]'.format(product.product_id, product.name,
                                        product.nutri_score.upper()))
        return prompt

    def display_products(self, products):
        prompt = 'Selectionnez un substitut : '
        for product in products:
            print()
            self.display_product(product)
        return prompt

    def display_substitute(self, product, substitute):
        if substitute:
            prompt = 'Enregistrer dans mes aliments substitués ? : '
            print('=== Aliment substitué ===')
            self.display_product(product)
            print('=== Aliment de substitution === ')
            self.display_product(substitute)
        else:
            prompt = None
            print('=== Aliment sélectionné ===')
            self.display_product(product)
            print('=== Aucun aliment de substitution trouvé ! ===')
        return prompt
