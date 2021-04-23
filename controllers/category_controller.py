#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.db_config as db_config
from database.database import Database


class CategoryController:

    def __init__(self):
        self.database = Database(db_config.SERVER_CONNECTION)

    def get(self):
        return self.database.get_categories()

    def set(self, categories):
        self.database.set_categories(categories)
