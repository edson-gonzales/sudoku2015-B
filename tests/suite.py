import unittest

import sys

sys.path.append("../../sudoku2015-B")

from backtracking_test import BacktrackingTest


backtracking_suite = unittest.TestLoader().loadTestsFromTestCase(BacktrackingTest)

alltests = unittest.TestSuite([backtracking_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)

