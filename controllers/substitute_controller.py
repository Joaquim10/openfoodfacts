#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from database.database import Database
from views.substitute_view import SubstituteView


class SubstituteController:

    def __init__(self):
        self.database = Database()
        self.substitute_view = SubstituteView()

    def get(self):
        return self.database.get_substitutes()

    def set(self, substitute):
        self.database.set_substitute(substitute)
