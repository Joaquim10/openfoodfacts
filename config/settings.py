#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""settings contains the settings of the application"""

# Product categories
# You can change, add and delete the product categories being used here.
# The valid categories can be found on this page:
# https://fr.openfoodfacts.org/categories.json
# On this page, you can filter the categories by name and develop all.
# This operation is slow.
#
CATEGORIES = [
    'Légumes et dérivés',
    'Plats à base de riz',
    'Viandes',
    'Fromages',
    'Desserts',
    'Petit-déjeuners'
]

MAX_PRODUCTS = 50

MAX_SUBSTITUTES = 6
