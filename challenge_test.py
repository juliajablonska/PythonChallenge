import unittest
import datetime as dt
from unittest.mock import patch
from io import StringIO

from challenge import start_past_check


class TestStartPastCheck(unittest.TestCase):

    def test_start_past_check_correct(self):
        time_in_future = dt.datetime.now() + dt.timedelta(days=10)
        self.assertEqual(start_past_check(time_in_future), time_in_future)

    def test_start_past_check_answer_yes(self):
        time_in_past = dt.datetime(2023, 11, 10, 18,0)
        with patch('builtins.input', return_value='yes'):
            self.assertEqual(start_past_check(time_in_past),time_in_past)

    def test_start_past_check_answer_no(self):
        time_in_past = dt.datetime(2023, 11, 10, 18, 0)
        time_in_future = dt.datetime.now() + dt.timedelta(days=10)
        with (
            patch('builtins.input', return_value='no'),
            patch('challenge.time_start', return_value=time_in_future)
        ):
            self.assertEqual(start_past_check(time_in_past),time_in_future)

    def test_start_past_check_wrong_input(self):
        time_in_past = dt.datetime(2023, 11, 10, 18, 0)
        with (
            patch('builtins.input', side_effect=["not sure","yes"]),
            patch('sys.stdout', new=StringIO()) as fake_out
        ):
            start_past_check(time_in_past)
            self.assertEqual(fake_out.getvalue().strip(), 'Wrong input, please try again')

if __name__ == '__main__':
    unittest.main()
