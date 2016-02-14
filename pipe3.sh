#!/bin/bash
time bzcat wc_day*_1.out.bz2 | awk '{print substr($4, 2, length($4)) " " $NF}' | python time.py 