#!/bin/bash
time bzcat wc_day*_1.out.bz2 | awk 'substr($(NF-1), 1, 1) == 3 || substr($(NF-1), 1, 1) == 2 {print $7}' | awk 'BEGIN{FS="/"} {$NF=""; print $0}' | sort | uniq -c | python tree.py
