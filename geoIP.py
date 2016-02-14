#!/usr/bin/env python
import GeoIP
import sys
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
for line in sys.stdin:
    print gi.country_code_by_addr(line.rstrip())# rstrip removes whitespace

    
