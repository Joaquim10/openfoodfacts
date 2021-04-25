#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MenuView:

    def __init__(self):
        pass

    @staticmethod
    def title():
        print ('\nPur Beurre - Powered by Open Food Facts !')

    @staticmethod
    def main_menu():
        prompt = '>>> '
        main_menu = [
            '    1 - Remplacer un aliment ...',
            '    2 - Voir mes aliments substitués',
            '    9 - Réinitialiser la base de données',
            '    0 - Quitter',
            'Quelle option choisissez-vous ?'
        ]
        for menu in main_menu:
            print(menu)
        return prompt
