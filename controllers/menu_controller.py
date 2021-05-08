#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.menu_view import MenuView


class MenuController:

    def __init__(self):
        self.menu_view = MenuView()

    @staticmethod
    def _select_option(prompt, options):
        option = '?'
        while option not in options:
            option = input(prompt)
        return int(option)

    def select_main_option(self):
        prompt = self.menu_view.display_main_menu()
        return self._select_option(prompt, '1290')

    def select_save_option(self):
        prompt = self.menu_view.display_save_menu()
        return self._select_option(prompt, '10')
