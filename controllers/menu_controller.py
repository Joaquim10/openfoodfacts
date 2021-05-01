#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.menu_view import MenuView


class MenuController:

    def __init__(self):
        self.menu_view = MenuView()

    def display_main_menu(self):
        return self.menu_view.display_main_menu()

    def display_save_menu(self):
        return self.menu_view.display_save_menu()

    @staticmethod
    def select(prompt, options):
        option = ''
        while option not in options or option == '':
            option = input(prompt)
        return option
