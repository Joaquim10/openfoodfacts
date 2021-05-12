#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

substitute: substitute contains the Substitute class.

Classes:
    Substitute: The Substitute object represents a substitute.
"""


class Substitute:
    """

    The Substitute object represents a substitute.

    Args:
        product_id (int): The product identifier.
        substitute_id (int): The substitute identifier.

    Attributes:
        product_id (int): The product identifier.
        substitute_id (int): The substitute identifier.
    """
    def __init__(self, product_id, substitute_id):
        self.product_id = product_id
        self.substitute_id = substitute_id
