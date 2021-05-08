#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MessageView:

    def __init__(self):
        self._caption()

    @staticmethod
    def _caption():
        caption = "Pur Beurre - Powered by Open Food Facts !"
        print(caption)

    @staticmethod
    def display_database_reset_message():
        message = "Réinitialisation de la base de données en cours..."
        print(message)
