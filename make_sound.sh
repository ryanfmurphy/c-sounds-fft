#!/bin/sh
php 1.c.php > 1php.c \
    && make 1php \
    && ./1php
# piping sound into stdout
