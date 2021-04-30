#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from views.category_view import CategoryView


class CategoryController:

    def __init__(self):
        self.database = Database()
        self.category_view = CategoryView()

    def get(self):
        return self.database.get_categories()

    def set(self, categories):
        self.database.set_categories(categories)

    def display(self, categories):
        return self.category_view.display(categories)

    @staticmethod
    def select(prompt, categories):
        category = ''
        while category not in categories or category == '':
            category = input(prompt)
        return category
