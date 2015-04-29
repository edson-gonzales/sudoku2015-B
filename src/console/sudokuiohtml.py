import sys, xml.etree.ElementTree as ElementTree
from xml.dom import minidom

sys.path.append("../../")

import unittest

from src.console.sudokuio import SudokuIO

class SudokuIOHtml(SudokuIO):

    def __init__(self, file_path):
        """ Creator method for the object this define the styles that will be used in 
        the table and the location of the file where the game will be saved.

        string file_path - The path where the sudoku game will be exported.
        """
        super(SudokuIOHtml, self).__init__(file_path)
        self.styles = [
            '.middle_line_row{\nborder-top-style: dotted;\nborder-top-width: 1px;\n' \
            'border-top-color: green;\n}\n',
            '.middle_line_col{\nborder-left-style: dotted;\nborder-left-width: 1px;\n' \
            'border-left-color: green;\n}\n',
            '.middle_line{\nborder-top-style: dotted;\nborder-top-width: 1px;\n' \
            'border-top-color: green;\nborder-left-style: dotted;\nborder-left-width: ' \
            '1px;\nborder-left-color: green;\n}\n'
            ]
        self.html_page = None

    def write(self, html_page):
        """ Method that write an ElementTree.Tree object in the file_path location file.

        ElementTree.Element html_page - The root of the page that will be saved in the 
            file_path location file
        """
        try:
            tree = ElementTree.ElementTree(html_page)
            tree.write(self.file_path)
        except IOError:
            print('The file' + self.file_path + 'does not exist')
    
    def build_page(self):
        """ This method build the tags for the html page.

        return ElementTree.Element - return the html_page variable with the root of 
            the page.
        """
        html_page = ElementTree.Element('html')
        html_head = ElementTree.SubElement(html_page, 'head')
        html_style = ElementTree.SubElement(html_head, 'style')
        html_style.text = ''.join(self.styles)
        html_title = ElementTree.SubElement(html_head, 'h2')
        html_title.text = 'Sudoku Exported Grid:'
        html_body = ElementTree.SubElement(html_page, 'body')
        html_table = ElementTree.SubElement(html_body, 'table')
        return html_page

    def __str__(self):
        """ Convert the class to string.

        return string - this method return an string representation of the class.
        """
        return ElementTree.tostring(self.html_page)

    @staticmethod
    def format_grid_to_string(grid):
        """ Method that evaluate a grid and return the string representation of the grid
            in html format

        int[9][9] grid - the grid that will be converted to string with html format.
        return string - the string representation with html tags of a grid.
        """
        html_page = SudokuIOHtml('./')
        html_page.format_grid(grid)
        return str(html_page)
    
    def format_grid(self, grid):
        """ Method that format the grid provided with html tags in a table.

        int[9][9] grid - the grid that will be converted to ElementTree.Element.
        return ElementTree.Element - return the root of the page.
        """
        self.html_page = None
        self.html_page = self.build_page()
        for table in self.html_page.iter('table'):
            self.table = table
            for row in range(len(grid)):
                html_row = self.fill_rows(grid, row, self.table)
        return self.html_page
        
    def fill_rows(self, grid, row, table):
        """ Method that fill the rows of the grid in the table.

        int[9][9] grid - the grid that will be converted to ElementTree.Element.
        int row - the row that will be evaluated in the grid.
        ElementTree.Element table - the current partial representation
            of the grid in html format.
        return ElementTree.Element - return the row of a table.
        """
        html_row = ElementTree.SubElement(self.table, 'tr')
        for col in range (len(grid[row])):
            if(col == len(grid[row])-1 and row % 3 == 0 and row >= 1):
                html_col = ElementTree.SubElement(html_row, 'td', {'class':'middle_line_row'})
                html_col.text = str(grid[row][col])
            elif (col % 3 == 0) and ((row % 3 != 0) or (row == 0)) and (col >= 1):
                html_col = ElementTree.SubElement(html_row, 'td', {'class':'middle_line_col'})
                html_col.text = str(grid[row][col])
            elif (col % 3 == 0) and (row % 3 == 0) and col >= 1 and row >= 1:
                html_col = ElementTree.SubElement(html_row, 'td', {'class':'middle_line'})
                html_col.text = str(grid[row][col])
            elif (row % 3 == 0) and ((col % 3 != 0) or (col == 0)) and (row >= 1):
                html_col = ElementTree.SubElement(html_row, 'td', {'class':'middle_line_row'})
                html_col.text = str(grid[row][col])
            else:
                html_col = ElementTree.SubElement(html_row, 'td')
                html_col.text = str(grid[row][col])
        return html_row

    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.

        ElementTree.Element elem - convert and ElementTree.Element in a string representation.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")