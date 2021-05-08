#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
from database.database import Database
from views.category_view import CategoryView


class CategoryController:

    def __init__(self):
        self.database = Database()
        self.category_view = CategoryView()

    def get_categories(self):
        self.database.set_categories(settings.CATEGORIES)
        return self.database.get_categories()

    @staticmethod
    def _select_category(prompt, categories):
        selected_category = None
        while not selected_category:
            option = input(prompt)
            for category in categories:
                if option == str(category.category_id):
                    selected_category = category
                    break
        return selected_category

    def select_category(self):
        categories = self.database.get_categories()
        prompt = self.category_view.display_categories(categories)
        return self._select_category(prompt, categories)
