#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

menu_controler: menu_controler contains the MenuController class.

Classes:
    MenuController: The MenuController object processes the menu controller.

Methods:
    select_main_option(): Gets a menu option from the main menu.
    select_save_option(): Gets a menu option from the save menu.
"""

from views.menu_view import MenuView


class MenuController:
    """

    The MenuController object initializes and processes the menu controller.

    Attributes:
        menu_view (menu_view.MenuView): The menu view.
    """
    def __init__(self):
        self.menu_view = MenuView()

    @staticmethod
    def _select_option(prompt, options):
        '''Asks the user for a menu option.'''
        option = ''
        while option not in options or option == '':
            option = input(prompt)
        return int(option)

    def select_main_option(self):
        '''

        Gets an option from the main menu.

        This method displays the main menu and asks the user for a menu
        option.

            Returns:
                option (int): The selected option.
        '''
        prompt = self.menu_view.display_main_menu()
        return self._select_option(prompt, '1290')

    def select_save_option(self):
        '''

        Gets an option from the save menu.

        This method displays the save menu and asks the user for a menu
        option.

            Returns:
                option (int): The selected option.
        '''
        prompt = self.menu_view.display_save_menu()
        return self._select_option(prompt, '10')
