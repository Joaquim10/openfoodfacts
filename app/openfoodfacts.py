#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.const as const
from app.database import Database
from app.category import Category

class OpenFoodFacts:

    def __init__(self):
        self.database = Database(const.DATABASE_SERVER_CONNECTION_CONFIG)

    def categories(self):
        categories = []
        for category in const.CATEGORIES:
            categories.append(Category(None, category))
        self.database.set_categories(categories)
        return self.database.get_categories()

    def run(self):
        categories = self.categories()

        for category in categories:
            print(category.category_id, category.name)
