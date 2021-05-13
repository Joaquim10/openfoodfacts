#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

category_controler: category_controler contains the CategoryController class.

Classes:
    CategoryController: The CategoryController object processes the category
    controller.

Methods:
    get_categories(): Gets all the categories from the database.
    set_categories(): Sets the categories to the database.
    select_category(): Gets a category from the category menu.
"""

from database.database import Database
from views.category_view import CategoryView


class CategoryController:
    """

    The CategoryController object initializes and processes the category
    controller.

    Attributes:
        database (database.Database): The database.
        category_view (category_view.CategoryView): The category view.
    """
    def __init__(self):
        self.database = Database()
        self.category_view = CategoryView()

    def get_categories(self):
        '''

        Gets all the categories from the database.

            Returns:
                categories (list [category.Category]): The categories.
        '''
        return self.database.get_categories()

    def set_categories(self):
        '''Sets the categories to the database.'''
        self.database.set_categories()

    @staticmethod
    def _select_category(prompt, categories):
        '''Asks the user for a category.'''
        selected_category = None
        while not selected_category:
            option = input(prompt)
            for category in categories:
                if option == str(category.category_id):
                    selected_category = category
                    break
        return selected_category

    def select_category(self):
        '''

        Gets a category from the category menu.

        This method gets all the categories from the database, then displays a
        menu of these categories and asks the user for a category and finally
        returns the selected category.

            Returns:
                category (category.Category): The selected category.
        '''
        categories = self.database.get_categories()
        prompt = self.category_view.display_categories(categories)
        return self._select_category(prompt, categories)
