#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from api.off import OFF


class ProductController:

    def __init__(self):
        pass

    @staticmethod
    def api_get(category, page_size):
        api = OFF()
        return api.get_products(category, page_size)

    @staticmethod
    def set(products):
        database = Database()
        database.set_products(products)
