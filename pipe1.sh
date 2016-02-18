#!/bin/bash
time parallel bzcat ::: wc_day*_1.out.bz2 | awk '$(NF-1)!=200  {print $(NF-1)}' | sort | uniq -c
