#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""The main module starts the app."""

from app.openfoodfacts import OpenFoodFacts


if __name__ == "__main__":
    openfoodfacts = OpenFoodFacts()
    openfoodfacts.run()
