#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function

import os
import json
import sys

status = False
try:
    import snap
    version = snap.Version
    i = snap.TInt(5)
    if i == 5:
        status = True
except:
    pass

if status:
    print "SUCCESS, your version of Snap.py is %s" % (version)
else:
    print "*** ERROR, no working Snap.py was found on your computer"


if __name__ == '__main__':
    main()
