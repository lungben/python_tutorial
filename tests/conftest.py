"""
This module is always executed automatically when pytest is started
"""

# set Pythonpath to include modue code
import sys
import os
new_path = os.path.abspath('../code')
if new_path not in sys.path:
    sys.path.append(new_path)

# import fixtures - must be after setting Pythonpath !
from fixtures import * # one of the few cases where import * is OK
# import more fixture files here, if required
