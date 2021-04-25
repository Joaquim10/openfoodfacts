#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.menu_view import MenuView


class MenuController:

    def __init__(self):
        pass

    @staticmethod
    def title():
        menu_view = MenuView()
        menu_view.title()

    @staticmethod
    def main_menu():
        menu_view = MenuView()
        return menu_view.main_menu()

    @staticmethod
    def prompt(prompt):
        return input(prompt)
