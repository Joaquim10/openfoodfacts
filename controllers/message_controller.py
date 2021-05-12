#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

message_controler: message_controler contains the MessageController class.

Classes:
    MessageController: The MessageController object processes the message
    controller.

Methods:
    display_database_reset_message(): Displays the database reset message.
"""

from views.message_view import MessageView


class MessageController:
    """

    The MessageController object initializes and processes the message
    controller.

    Attributes:
        message_view (message_view.MessageView): The message view.
    """
    def __init__(self):
        self.message_view = MessageView()

    def display_database_reset_message(self):
        '''Displays the database reset message.'''
        self.message_view.display_database_reset_message()
