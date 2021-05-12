#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

menu_view: menu_view contains the MenuView class.

Classes:
    MenuView: The MenuView object processes the menu view.
"""


class MenuView:
    """The MenuView object initializes and processes the menu view."""
    def __init__(self):
        pass

    @staticmethod
    def _display_menu(menu):
        '''Displays the menu and returns the prompt.'''
        print()
        for option in menu:
            print("{}".format(option))
        prompt = "Selectionnez une option : "
        return prompt

    def display_main_menu(self):
        '''
        Displays the main menu and returns the prompt.

        Returns:
            prompt (str): The prompt.
        '''
        main_menu = [
            "1 - Remplacer un aliment...",
            "2 - Voir mes aliments substitués",
            "9 - Réinitialiser la base de données",
            "0 - Quitter"
        ]
        return self._display_menu(main_menu)

    def display_save_menu(self):
        '''
        Displays the save menu and returns the prompt.

        Returns:
            prompt (str): The prompt.
        '''
        save_menu = [
            "1 - Enregister dans mes aliments substitués",
            "0 - Revenir au menu principal"
        ]
        return self._display_menu(save_menu)
