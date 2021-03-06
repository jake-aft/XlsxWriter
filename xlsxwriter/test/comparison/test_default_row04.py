###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2020, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('default_row04.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.set_default_row(24)

        worksheet.write('A1', 'Foo')
        worksheet.write('A10', 'Bar')

        worksheet.write_comment('C4', 'Hello', {'y_offset': 22})

        worksheet.set_comments_author('John')

        workbook.close()

        self.assertExcelEqual()
