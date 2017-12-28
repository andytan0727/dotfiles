#!/bin/sh

#
# ~/.xsession
#
#

[[ -f ~/.extend.xsession ]] && . ~/.extend.xsession
xset r rate 250 25  # faster key rate
