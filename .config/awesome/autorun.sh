#!/bin/sh

# run() {
#   if ! pgrep -f "$1" ;
#   then
#     "$@"&
#   fi
# }

# run "flameshot" ;
# 
# run "picom --experimental-backends" ;
# 
# run "wal -R" ;
# 
# run "conky -c ~/.config/conky/themes/minimal-clear/dark-minimal-clear.conf" ;

flameshot &
wal -R &
#conky -c ~/.config/conky/themes/minimal-clear/dark-minimal-clear.conf &
picom --experimental-backends &
fcitx5
