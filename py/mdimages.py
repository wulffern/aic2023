#!/usr/bin/env python3

import sys
import re

for l in sys.stdin:

    m = re.search("!\[[^\]]+\]\((.*)\)",l)
    if(m):
        url = m.group(1)
        if(re.search("(^http:|/ip/)",url)):
            continue

        print(m.group(1))
