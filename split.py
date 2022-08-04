#!/usr/bin/env python3

import sys

links = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
sys.stdout.write(links.replace("https", " https"))

