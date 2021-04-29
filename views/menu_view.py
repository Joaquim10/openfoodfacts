#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MenuView:

    def __init__(self):
        pass

    @staticmethod
    def display():
        main_menu = [
            '1 - Remplacer un aliment...',
            '2 - Voir mes aliments substitués',
            '9 - Réinitialiser la base de données',
            '0 - Quitter'
        ]
        prompt = 'Selectionnez une option : '
        for menu in main_menu:
            print('    {}'.format(menu))
        return prompt
