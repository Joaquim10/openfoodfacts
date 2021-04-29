#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MessageView:

    def __init__(self):
        caption = 'Pur Beurre - Powered by Open Food Facts !'
        self.caption(caption)

    def caption(self, caption):
        print ('\n', caption)

    def message(self, message):
        print (message)
