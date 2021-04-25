#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Product:

    # def __init__(self, product_id, name, category_id, nutri_score, url
    #              description=None, stores=None)
    def __init__(self, product):
        self.product_id = product['product_id']
        self.name = product['name']
        self.category_id = product['category_id']
        if 'description' in product:
            self.description = product['description']
        else:
            self.description = None
        self.nutri_score = product['nutri_score']
        if 'stores' in product:
            self.stores = product['stores']
        else:
            self.stores = None
        self.url = product['url']
