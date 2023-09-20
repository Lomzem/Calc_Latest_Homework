from datetime import date
from calc_2_hw import find_latest_date
import pandas as pd
import unittest

class TestFindLatestDate(unittest.TestCase):
    def test_before_earliest_date(self):
        current_date = date(2023, 1, 1)
        dates = pd.date_range(date(2023, 1, 2), date(2023, 1, 3)).date
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, 0)

    def test_on_earliest_date(self):
        current_date = date(2023, 1, 2)
        dates = pd.date_range(date(2023, 1, 2), date(2023, 1, 3)).date
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, 0)

    def test_after_last_date(self):
        current_date = date(2023, 1, 9)
        dates = pd.date_range(date(2023, 1, 2), date(2023, 1, 3)).date
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, -1)

    def test_between_two_dates(self):
        current_date = date(2023, 1, 3)
        dates = [date(2023, 1, 2), date(2023, 1, 4), date(2023, 1, 5), date(2023, 1, 6)]
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, 1)

    def test_on_due_date(self):
        current_date = date(2023, 1, 5)
        dates = [date(2023, 1, 2), date(2023, 1, 4), date(2023, 1, 5), date(2023, 1, 6)]
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, 2)

    def test_on_last_date(self):
        current_date = date(2023, 1, 6)
        dates = [date(2023, 1, 2), date(2023, 1, 4), date(2023, 1, 5), date(2023, 1, 6)]
        result = find_latest_date(dates, current_date)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
