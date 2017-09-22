#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
        
    line = line.strip()
    # split the line into words
    try:
    	id, labels, text = line.split('\t', 2)
    except:
	    continue
    # increase counters
    print '%s\t%s' % (id, labels)
