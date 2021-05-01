#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MenuView:

    def __init__(self):
        pass

    @staticmethod
    def display_menu(menu):
        prompt = "Selectionnez une option : "
        for option in menu:
            print("{}".format(option))
        return prompt

    def display_main_menu(self):
        main_menu = [
            "1 - Remplacer un aliment...",
            "2 - Voir mes aliments substitués",
            "9 - Réinitialiser la base de données",
            "0 - Quitter"
        ]
        print()
        return self.display_menu(main_menu)

    def display_save_menu(self):
        save_menu = [
            "1 - Enregister dans mes aliments substitués",
            "2 - Revenir au menu principal"
        ]
        return self.display_menu(save_menu)
