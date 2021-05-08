#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MenuView:

    def __init__(self):
        pass

    @staticmethod
    def _display_menu(menu):
        print()
        for option in menu:
            print("{}".format(option))
        prompt = "Selectionnez une option : "
        return prompt

    def display_main_menu(self):
        main_menu = [
            "1 - Remplacer un aliment...",
            "2 - Voir mes aliments substitués",
            "9 - Réinitialiser la base de données",
            "0 - Quitter"
        ]
        return self._display_menu(main_menu)

    def display_save_menu(self):
        save_menu = [
            "1 - Enregister dans mes aliments substitués",
            "0 - Revenir au menu principal"
        ]
        return self._display_menu(save_menu)
