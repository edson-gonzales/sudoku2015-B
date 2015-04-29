import unittest

import sys

sys.path.append("../tests")

from backtracking_test import BacktrackingTest
from Algorithm_Brute_Force_Test import TestBruteForceAlgorithm
from Peter_Norvig_Test import PeterNorvigTest
from read_config_file_test import ReadConfigFileTest
from sudokuio_test import SudokuIOTest
from sudokuiohtml_test import SudokuIOHtmlTest


backtracking_suite = unittest.TestLoader().loadTestsFromTestCase(BacktrackingTest)
algorithm_brute_force_suite = unittest.TestLoader().loadTestsFromTestCase(TestBruteForceAlgorithm)
peter_norvig_suite = unittest.TestLoader().loadTestsFromTestCase(PeterNorvigTest)
read_confg_file = unittest.TestLoader().loadTestsFromTestCase(ReadConfigFileTest)
sudoku_io_suite = unittest.TestLoader().loadTestsFromTestCase(SudokuIOTest)
sudku_io_html = unittest.TestLoader().loadTestsFromTestCase(SudokuIOHtmlTest)

alltests = unittest.TestSuite([backtracking_suite,algorithm_brute_force_suite,read_confg_file,peter_norvig_suite,sudoku_io_suite,sudku_io_html])

unittest.TextTestRunner(verbosity=1).run(alltests)

