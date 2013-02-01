import unittest
from StringIO import StringIO
import gen

class GenTest(unittest.TestCase):
    def test_gen(self):
        '''Should parse a multi-file stream into separate sections'''
        s = StringIO('-- test.txt\nfile contents\nmore contents\n-- test2.txt\ntest2 contents\nmore stuff\n')
        self.assertDictEqual(gen.parse(s, '--'), { 'test.txt': 'file contents\nmore contents\n', 'test2.txt': 'test2 contents\nmore stuff\n' })

