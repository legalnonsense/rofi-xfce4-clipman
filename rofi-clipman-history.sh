#!/bin/bash

open=$(rofi-clipman-history-splitter.py | rofi -dmenu "$@" -no-sort -l 50 -i -p "Copy:" format -q -width 2500)
echo $open | xclip -sel clip









