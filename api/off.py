#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

off: off contains the OFF class.

Classes:
    OFF: The OFF object processes Open Food Facts API requests and
    json format data.

    Methods:
        get_products(category, page_size):
            Gets a page of products from the specified category from the
            Open Food Facts API.
"""

import requests

from models.product import Product


class OFF:
    """

    The OFF object processes Open Food Facts API requests and json format
    data.
    """
    def __init__(self):
        pass

    @staticmethod
    def _get_products(category, page_size):
        '''

        Gets a page of products in a json format from the specified category
        from the Open Food Facts API.
        The subdomain used for the query is 'fr'.
        '''
        url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category.name,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'page_size': page_size,
            'json': 'true',
            'User-Agent': "Pur Beurre - Linux - Version 1.0"
        }
        request = requests.get(url, params=payload)
        return request.json().get('products')

    @staticmethod
    def _check_integrity(category, api_products):
        '''Gets cleaned products extracted from a json format.'''
        products = []
        for api_product in api_products:
            product = {
                'product_id': None,
                'name': None,
                'category_id': category.category_id,
                'description': '',
                'nutri_score': None,
                'stores': '',
                'url': None
            }
            product = Product(product)
            if 'product_name_fr' in api_product or \
                    'product_name' in api_product:
                if api_product['product_name_fr'] != '':
                    product.name = api_product['product_name_fr']
                elif api_product['product_name'] != '':
                    product.name = api_product['product_name']
            if 'generic_name_fr' in api_product:
                product.description = api_product['generic_name_fr']
            elif 'generic_name' in api_product:
                product.description = api_product['generic_name']
            if 'nutrition_grade_fr' in api_product:
                if api_product['nutrition_grade_fr'] in 'abcdeABCDE':
                    product.nutri_score = api_product['nutrition_grade_fr']
            if 'stores' in api_product:
                product.stores = api_product['stores']
            if 'url' in api_product:
                if 'https://fr.openfoodfacts.org/produit/' in \
                                                api_product['url'].lower():
                    product.url = api_product['url']
            if product.name and product.nutri_score and product.url:
                products.append(product)
        return products

    def get_products(self, category, page_size):
        '''

        Gets a page of products from the specified category from the
        Open Food Facts API.

        This method gets a page of products in a json format from the
        specified category from the Open Food Facts API, then extracts the
        products from the json format, checks their integrity and returns the
        cleaned products.

            Args:
                category (category.Category): The category.
                page_size (int): Maximum number of products.

            Returns:
                products (list [product.Product]): The products.
        '''
        products = self._get_products(category, page_size)
        return self._check_integrity(category, products)
