#!/bin/bash
time parallel bzcat ::: wc_day*_1.out.bz2  | cut -d ' ' -f 1 | python geoIP.py | sort | uniq -c | sort -b -n -r | head -n 10
