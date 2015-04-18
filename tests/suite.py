import unittest, coverage

import sys

sys.path.append("../../sudoku2015-B")
cov = coverage.coverage()
cov.start()

from backtracking_test import BacktrackingTest


backtracking_suite = unittest.TestLoader().loadTestsFromTestCase(BacktrackingTest)

alltests = unittest.TestSuite([backtracking_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)

cov.stop()
cov.save()

cov.html_report()