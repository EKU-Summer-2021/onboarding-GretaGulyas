import unittest
import pandas as pd
from src.csv_read import read_csv_pandas

class CSVReadDataTets(unittest.TestCase):

    def test_csv(self):
        # given
        EXPECTED = True
        # when
        ACTUAL = isinstance(read_csv_pandas(), pd.DataFrame)
        # then
        self.assertEqual(EXPECTED, ACTUAL)
