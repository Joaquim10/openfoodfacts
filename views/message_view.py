#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MessageView:

    def __init__(self):
        caption = 'Pur Beurre - Powered by Open Food Facts !'
        self.caption(caption)

    @staticmethod
    def caption(caption):
        print('\n', caption)

    @staticmethod
    def message(message):
        print(message)
