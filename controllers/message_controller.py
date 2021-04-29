#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from views.message_view import MessageView


class MessageController:

    def __init__(self):
        self.message_view = MessageView()

    def message(self, message):
        self.message_view.message(message)
