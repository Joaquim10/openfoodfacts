#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""settings contains the settings of the application."""

# Product categories.
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

# Maximum number of products per category.
MAX_PRODUCTS = 50

# Maximum number of potential substitutes for replacing a product.
MAX_SUBSTITUTES = 6

# country code top-level domain of the subdomain for Open Food Facts API
# endpoints.
# Examples: 'world', 'us', 'fr'...
SUBDOMAIN = 'fr'

# User-Agent HTTP Header with the name of the app, the version, system
# and a url (if any) for Open Food Facts API.
USER_AGENT = 'Pur Beurre - Linux - Version 1.0'

# SQL Script file name
SQL_SCRIPT = 'openfoodfacts.sql'
