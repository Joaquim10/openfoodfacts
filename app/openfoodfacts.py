#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import config.settings as settings
# from models.category import Category
from controllers.category_controller import Category_Controller

class OpenFoodFacts:

    def __init__(self):
        self.categories = self.init_categories(settings.CATEGORIES)

    def init_categories(self, category_names):
        category_controller = Category_Controller()
        category_controller.set_categories(category_names)
        return category_controller.get_categories()
        
    def run(self):

        # Test
        for category in self.categories:
            print(category.category_id, category.name)
