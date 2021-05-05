# This script shows the tutorial of text wraping 

import textwrap

def texter(s, width_s):
    return textwrap.fill(s, width=width_s)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(texter(s, 4))