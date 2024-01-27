"""Full Doku on: https://github.com/NapoII/Rust-Collection"
-----------------------------------------------
!!! ADD MUST HAVE INFO !!
------------------------------------------------
"""

#### import

import os
import sys

from util.__funktion__ import *


#### pre Var

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = file_path + os.path.sep + "cfg"+ os.path.sep +"config.ini"

BSP_config = read_config(config_dir, "Test", "abc")


#### Main
# Rust-Collection.py
log(f'Programme has been started!','green')
