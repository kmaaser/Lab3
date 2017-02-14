#----------------------------------------------------------------------
# test_LList.py
# Karenna Maaser
# 02/13/2012
#----------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '..')
from LList import *

class testLList(unittest.TestCase):

    #----------------------------------------------------------------------

    def testLen(self):
        a = LList()
        a.append(1)
        a.append(2)
        a.append(3)

        self.assertEqual(a.LList, 3)

    #----------------------------------------------------------------------

def main(argv):
    unittest.main()

if __name__ == '__name__':
    main(sys.argv)