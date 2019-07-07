"""
This module is always executed automatically when pytest is started
"""

# set Pythonpath to include modue code
import sys
import os
new_paths = [os.path.abspath('../code'), os.path.abspath('../tests'),]
for new_path in new_paths:
    if new_path not in sys.path:
        sys.path.append(new_path)

# import fixtures and utils
from fixtures import * # one of the very few cases where import * is OK
