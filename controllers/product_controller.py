#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.db_config as db_config
from database.database import Database
from api.off import OFF


class ProductController:

    def __init__(self):
        self.database = Database(db_config.SERVER_CONNECTION)

    def api_get_products(self, category, page_size):
        api = OFF()
        return api.get_products(category, page_size)
