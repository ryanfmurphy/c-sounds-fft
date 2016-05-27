#!/bin/sh
sh make_sound.sh \
    | python -u fastfour.py \
    | ./play_sound.sh

