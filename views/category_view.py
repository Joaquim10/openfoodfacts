#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class CategoryView:

    def __init__(self):
        pass

    @staticmethod
    def display(categories):
        prompt = "Selectionnez une catégorie : "
        for category in categories:
            print("{} - {}".format(category.category_id, category.name))
        return prompt
