"""
oooooh so cheaty

runs all math through bc, giving precise
floating point numbers for any and all
equations

http://www.gnu.org/software/bc/manual/html_mono/bc.html
"""

math = raw_input("Input math: ")
program = "bc " + math + " | more"

import subprocess
subprocess.call([program])
