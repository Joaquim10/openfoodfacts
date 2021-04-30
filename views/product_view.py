#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class ProductView:

    def __init__(self):
        pass

    @staticmethod
    def display(products):
        prompt = 'Selectionnez un produit : '
        for product in products:
            print('    {} - {}'.format(product.product_id, product.name))
        return prompt

    @staticmethod
    def display_detailed(product, category):
        print('    Nom         : {}'.format(product.name))
        print('    Description : {}'.format(product.description))
        print('    Catégorie   : {}'.format(category.name))
        print('    Numéro      : {}'.format(product.product_id))
        print('    Nutri-score : {}'.format(product.nutri_score.upper()))
        magasins = ', '.join(product.stores.split(','))
        print('    Magasins    : {}'.format(magasins))
        print('    Lien        : {}'.format(product.url))
