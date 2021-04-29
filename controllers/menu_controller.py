#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.menu_view import MenuView


class MenuController:

    def __init__(self):
        pass

    @staticmethod
    def display():
        menu_view = MenuView()
        return menu_view.display()

    @staticmethod
    def select(prompt, keys):
        key = ''
        while key == '' or key not in keys:
            key = input(prompt)
        return key
