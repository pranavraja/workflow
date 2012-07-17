#!/usr/bin/env python
import sys
import os

DELIMITER = '--'

def write_files(input_filename):
	current_file = None
	for line in open(input_filename):
		if not line.strip(): continue
		if line.startswith(DELIMITER):
			current_filename = os.path.join(os.path.dirname(input_filename), line[len(DELIMITER):].strip())
			current_file = open(current_filename, 'w')
		elif current_file:
			current_file.write(line)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: python %s input_file' % __file__
		sys.exit(0)
	input_file = sys.argv[1]
	write_files(open(input_file))
