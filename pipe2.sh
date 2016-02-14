#!/bin/bash
time bzcat wc_day*_1.out.bz2  | cut -d ' ' -f 1 | python geoIP.py | sort | uniq -c | sort -b -n -r | head -n 10
#parallel bzcat ::: wc_day6_1.out.bz2 wc2_day6_1.out.bz2  for parallel
#| tail -n 6 
