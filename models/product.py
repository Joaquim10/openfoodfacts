#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

product: product contains the Product class.

Classes:
    Product: The Product object represents a product.
"""


class Product:
    """

    The Product object represents a product.

    Args:
        product (dict):
        The keyword arguments are used to initialize the product.
            ['product_id'] (int): The product identifier.
            ['name'] (str): The name.
            ['category_id'] (int): The category identifier.
            ['description'] (str): The description (optional).
            ['nutri_score'] (str): The nutri-score.
            ['stores'] (str): The stores (optional).
            ['url'] (str): The url.

    Attributes:
        product_id (int): The product identifier.
        name (str): The name.
        category_id (int): The category identifier.
        description (str): The description.
        nutri_score (str): The nutri-score.
        stores (str): The stores.
        url (str): The url.
    """
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
