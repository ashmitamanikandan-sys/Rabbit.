# -*- coding: utf-8 -*-
"""
make_hero_catalog.py
Compiles all 36 Hero Books with 6-8 chapters each.
Validates zero banned phrases and valid connects_to internally.
"""

import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

# We will construct all 36 Hero Books in clean structured dictionaries
# and export them to hero_books.json so they can be seamlessly loaded by build_all_catalog.py
