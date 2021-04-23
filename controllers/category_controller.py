#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.db_config as db_config
from database.database import Database
from models.category import Category


class CategoryController:

    def __init__(self):
        self.database = Database(db_config.SERVER_CONNECTION)

    def get(self):
        return self.database.get_categories()

    def set(self, category_names):
        categories = []
        for category in category_names:
            categories.append(Category(None, category))
        self.database.set_categories(categories)
