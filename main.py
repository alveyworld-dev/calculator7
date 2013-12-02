"""
oooooh so cheaty

runs all math through bc, giving precise
floating point numbers for any and all
equations
"""

math = raw_input("Input math: ")
program = "bc " + math + " | more"

import subprocess
subprocess.call([program])
