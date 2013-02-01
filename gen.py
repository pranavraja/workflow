#!/usr/bin/env python
import sys
import os
from collections import defaultdict

def parse(f, delimeter):
    files = defaultdict(str)
    current_filename = None
    for line in f:
        if not line.strip(): continue
        if line.startswith(delimeter):
            current_filename = line[len(delimeter):].strip()
        elif current_filename:
            files[current_filename] += line
    return files

def create(d, basepath):
    if not os.path.isdir(basepath):
        os.mkdir(basepath)
    for filename, content in d.items():
        open(os.path.join(basepath, filename), 'w').write(d[filename])

