#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MessageView:

    def __init__(self):
        self.caption()

    @staticmethod
    def caption():
        caption = "Pur Beurre - Powered by Open Food Facts !"
        print("\n", caption)

    @staticmethod
    def database_reset():
        message = "Réinitialisation de la base de données en cours..."
        print(message)
