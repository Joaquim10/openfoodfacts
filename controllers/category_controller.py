#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database


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
