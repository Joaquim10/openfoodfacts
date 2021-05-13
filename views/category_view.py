#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

category_view: category_view contains the CategoryView class.

Classes:
    CategoryView: The CategoryView object processes the category view.

Methods:
    display_categories(categories):
        Displays the specified categories and returns the prompt.

"""


class CategoryView:
    """The CategoryView object initializes and processes the category view."""
    def __init__(self):
        pass

    @staticmethod
    def display_categories(categories):
        '''
        Displays the specified categories and returns the prompt.

        Args:
            categories (list [category.Category]): The categories.

        Returns:
            prompt (str): The prompt.
        '''
        print()
        for category in categories:
            print("{} - {}".format(category.category_id, category.name))
        prompt = "Selectionnez une catégorie : "
        return prompt
