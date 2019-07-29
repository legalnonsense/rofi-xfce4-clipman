#!/usr/bin/env python3
import re
import sys
from os.path import expanduser

with open(expanduser("~") + "/.cache/xfce4/clipman/textsrc", "r") as f:
    textsrc = f.read()

entries=re.split(r"(?!\\);", textsrc)

for entry in reversed(entries):
    if entry == '':
        pass 
    else:
        sys.stdout.write(entry.replace("\\s", " ").replace("\\n", "\n").replace("\\;", ""))

