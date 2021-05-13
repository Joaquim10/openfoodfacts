#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

message_view: message_view contains the MessageView class.

Classes:
    MessageView: The MessageView object processes the message view.

Methods:
    display_database_reset_message():
        Displays the database reset message.
"""


class MessageView:
    '''The MessageView object initializes and processes the message view.'''
    def __init__(self):
        self._caption()

    @staticmethod
    def _caption():
        '''Displays the caption.'''
        caption = "Pur Beurre - Powered by Open Food Facts !"
        print(caption)

    @staticmethod
    def display_database_reset_message():
        '''Displays the database reset message.'''
        message = "Réinitialisation de la base de données en cours..."
        print(message)
