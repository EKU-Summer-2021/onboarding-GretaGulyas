import unittest

import pandas as pd

from src.csv_read import read_csv_pandas


class CSVReadDataTets(unittest.TestCase):

    def test_csv(self):
        # given
        EXPECTED = True
        # when
        ACTUAL = isinstance(read_csv_pandas('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_100.csv'), pd.DataFrame)
        # then
        self.assertEqual(EXPECTED, ACTUAL)
