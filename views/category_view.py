#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class CategoryView:

    def __init__(self):
        pass

    @staticmethod
    def display_categories(categories):
        print()
        for category in categories:
            print("{} - {}".format(category.category_id, category.name))
        prompt = "Selectionnez une catégorie : "
        return prompt
