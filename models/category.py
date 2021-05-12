#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

category: category contains the Category class.

Classes:
    Category: The Category object represents a category.
"""


class Category:
    """

    The Category object represents a category.

    Args:
        category_id (int): The category identifier.
        name (str): The name.

    Attributes:
        category_id (int): The category identifier.
        name (str): The name.
    """
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
