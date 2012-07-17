#!/usr/bin/env python
from ConfigParser import RawConfigParser
import os
import sys
import webbrowser
import gen

def write_flow_from_cfg(cfg, out_dir):
	parser = RawConfigParser()
	parser.read(cfg)
	if not os.path.isdir(out_dir):
		os.mkdir(out_dir)
	filename = os.path.join(out_dir, 'out.txt')
	f = open(filename, 'w')
	for section in parser.sections():
		f.write('-- %s.html\n<h1>%s</h1>\n' % (section, section))
		if parser.has_option(section, 'message'):
			f.write('<p>%s</p>\n' % parser.get(section, 'message'))
		for option in parser.options(section):
			if option == 'message': continue
			f.write('<a href="%s.html">%s</a><br>\n' % (parser.get(section, option), option))
	f.close()
	gen.write_files(filename)
	return os.path.join(out_dir, '%s.html' % parser.sections()[0])

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Example usage: python %s cfg.cfg out' % __file__
		sys.exit(0)
	conf = sys.argv[1]
	out_dir = sys.argv[2]
	start = write_flow_from_cfg(conf, out_dir)
	webbrowser.open('file://%s' % os.path.abspath(start))

