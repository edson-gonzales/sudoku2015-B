import unittest

import sys

sys.path.append("../tests")

from backtracking_test import BacktrackingTest
from Algorithm_Brute_Force_Test import TestBruteForceAlgorithm
from Peter_Norvig_Test import PeterNorvigTest
from read_config_file_test import ReadConfigFileTest
from sudokuio_test import SudokuIOTest
from sudokuiohtml_test import SudokuIOHtmlTest
from save_config_file_test import SaveConfigFileTest
from sudokuiocsv_test import SudokuIOCsvTest


backtracking_suite = unittest.TestLoader().loadTestsFromTestCase(BacktrackingTest)
algorithm_brute_force_suite = unittest.TestLoader().loadTestsFromTestCase(TestBruteForceAlgorithm)
peter_norvig_suite = unittest.TestLoader().loadTestsFromTestCase(PeterNorvigTest)
read_confg_file_suit = unittest.TestLoader().loadTestsFromTestCase(ReadConfigFileTest)
save_confg_file_suit = unittest.TestLoader().loadTestsFromTestCase(SaveConfigFileTest)
sudoku_io_suite = unittest.TestLoader().loadTestsFromTestCase(SudokuIOTest)
sudoku_io_html_suit = unittest.TestLoader().loadTestsFromTestCase(SudokuIOHtmlTest)
sudoku_io_csv_suit = unittest.TestLoader().loadTestsFromTestCase(SudokuIOCsvTest)
sudoku_generator_brute_force_html_suit = unittest.TestLoader().loadTestsFromTestCase(TestBruteForceAlgorithm)

alltests = unittest.TestSuite([
	backtracking_suite,
	algorithm_brute_force_suite,
	read_confg_file_suit,
	peter_norvig_suite,
	sudoku_io_suite,
	sudoku_io_html_suit,
	save_confg_file_suit,
	sudoku_io_csv_suit,
	sudoku_generator_brute_force_html_suit
	])

unittest.TextTestRunner(verbosity=1).run(alltests)

