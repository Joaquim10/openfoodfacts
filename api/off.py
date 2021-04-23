#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests


class OFF:

    def __init__(self):
        pass

    def get_products(self, category, page_size):
        url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'page_size': page_size,
            'json': 'true',
        }
        request = requests.get(url, params=payload)
        return request.json().get('products')
