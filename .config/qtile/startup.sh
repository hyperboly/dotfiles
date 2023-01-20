#!/bin/bash

picom &
flameshot &
fcitx5 -d &
#sh ~/.local/bin/daynightWall.sh & 
exec /usr/bin/dunst &
