import unittest
import pandas as pd
from src.Read_CSV_Pandas import read_csv_pandas

class CSVReadDataTets(unittest.TestCase):

    def test_csv(self):
        # given
        EXPECTED = True
        # when
        ACTUAL = isinstance(read_csv_pandas(), pd.DataFrame)
        # then
        self.assertEqual(EXPECTED, ACTUAL)

    # def test_fails(self):
    #     self.assertEqual(True, False)