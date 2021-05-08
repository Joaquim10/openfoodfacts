#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.message_view import MessageView


class MessageController:

    def __init__(self):
        self.message_view = MessageView()

    def display_database_reset_message(self):
        self.message_view.display_database_reset_message()
