#!/usr/bin/env python
from ConfigParser import RawConfigParser
import os
import sys
import webbrowser
import gen
from collections import defaultdict

def flow_from_cfg(cfg):
    files = defaultdict(str)
    for section in cfg.sections():
        filename = '{}.html'.format(section)
        files[filename] += '<h1>{}</h1>\n'.format(section)
        if cfg.has_option(section, 'message'):
            files[filename] += '<p>{}</p>\n'.format(cfg.get(section, 'message'))
        for option in cfg.options(section):
            if option == 'message': continue
            files[filename] += '<a href="{}.html">{}</a><br>\n'.format(cfg.get(section, option), option)
    return files

def conf_from_file(cfg_file):
    cfg = RawConfigParser()
    cfg.read(cfg_file)
    return cfg

def write_flow(cfg, output_dir):
    gen.create(flow_from_cfg(cfg), output_dir)

def start_page(cfg):
    return cfg.sections()[0]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Example usage: python %s cfg.cfg out' % __file__
        sys.exit(0)
    conf = sys.argv[1]
    out_dir = sys.argv[2]
    cfg = conf_from_file(conf)
    write_flow(cfg, out_dir)
    webbrowser.open('file://%s.html' % os.path.abspath(os.path.join(out_dir, start_page(cfg))))

