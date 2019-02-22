#!/bin/sh

conky -c ~/.config/conky/maia_cyan/system/conky_system.conf &
conky -c ~/.config/conky/maia_cyan/clock/conky_clock.conf &
conky -c ~/.config/conky/maia_cyan/cal/conky_cal.conf &
conky -c ~/.config/conky/maia_cyan/todo/conky_todo.conf &
# wait network to be connected
conky -p 30 -c ~/.config/conky/maia_cyan/speed/conky_speed.conf &

exit 0
