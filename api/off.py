#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

off: off contains the OFF class.

Classes:
    OFF: The OFF object processes Open Food Facts API requests.

    Methods:
        get_products(category):
            Gets a page of products in a json format from the specified
            category from the Open Food Facts API.
"""

import requests
import config.settings as settings


class OFF:
    """The OFF object processes Open Food Facts API requests."""
    def __init__(self):
        pass

    @staticmethod
    def get_products(category):
        '''

        Gets a page of products in a json format from the specified category
        from the Open Food Facts API.

            Args:
                category (category.Category): The category.

            Returns:
                products (json): The products.
        '''
        endpoint = [
            'https://',
            settings.SUBDOMAIN,
            '.openfoodfacts.org/cgi/search.pl'
        ]
        url = ''.join(endpoint)
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category.name,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'page_size': settings.MAX_PRODUCTS,
            'json': 'true',
            'User-Agent': settings.USER_AGENT
        }
        request = requests.get(url, params=payload)
        return request.json().get('products')
