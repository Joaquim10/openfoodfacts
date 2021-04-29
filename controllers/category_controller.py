#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from views.category_view import CategoryView


class CategoryController:

    def __init__(self):
        pass

    @staticmethod
    def get():
        database = Database()
        return database.get_categories()

    @staticmethod
    def set(categories):
        database = Database()
        database.set_categories(categories)

    @staticmethod
    def display(categories):
        category_view = CategoryView()
        return category_view.display(categories)

    @staticmethod
    def select(prompt, categories):
        category = ''
        while category == '' or category not in categories:
            category = input(prompt)
        return category
