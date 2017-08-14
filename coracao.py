#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import time
import random

# Colors
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8./800)

print "\n\n"

slowprint (P+"\t                 ******     ******      "+O)
slowprint (P+"\t              **********   **********    "+O)
slowprint (P+"\t            ************* *************  "+O)
slowprint (P+"\t           ***************************** "+O)
slowprint (P+"\t           ***************************** "+O)
slowprint (P+"\t           ***************************** "+O)
slowprint (P+"\t            ***************************  "+O)
slowprint (P+"\t              ***********************    "+O)
slowprint (P+"\t                *******************      "+O)
slowprint (P+"\t                  ***************        "+O)
slowprint (P+"\t                    ***********          "+O)
slowprint (P+"\t                      *******            "+O)
slowprint (P+"\t                        ***               "+O)
slowprint (P+"\t                         *                "+O)
print "\n\n"
slowprint (O+"\t                    AI CAMILA...          "+O)
slowprint (O+"\t                    VOCÊ É TÃO...          "+O)
slowprint (O+"\t                      LINDA!               "+O)
print "\n\n"
