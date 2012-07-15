
from ConfigParser import RawConfigParser
import os
import sys
import webbrowser

def write_flow_from_cfg(cfg, out_dir):
    parser = RawConfigParser()
    parser.read(cfg)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    for section in parser.sections():
        f = open(os.path.join(out_dir, '%s.html' % section), 'w')
        f.write('<h1>%s</h1>\n' % section)
        if parser.has_option(section, 'message'):
            f.write('<p>%s</p>\n' % parser.get(section, 'message'))
        for option in parser.options(section):
            if option == 'message': continue
            f.write('<a href="%s.html">%s</a><br>\n' % (parser.get(section, option), option))
        f.close()
    return os.path.join(out_dir, '%s.html' % parser.sections()[0])

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: python %s config_file out_dir' % __file__
        sys.exit(0)
    conf = sys.argv[1]
    out_dir = sys.argv[2]
    start = write_flow_from_cfg(conf, out_dir)
    webbrowser.open(start)

