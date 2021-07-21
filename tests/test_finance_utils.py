import unittest
import sys
sys.path.insert(1,"../")
import f_utils


class TestFinanceUtils(unittest.TestCase):
    def test_price_action(self):
        from f_utils import price_action
        import pandas as pd
        data = price_action(token_path = "../resources/token.txt", ticker = "PLTR")
        print(data.head())
        self.assertTrue(isinstance(data, pd.DataFrame))

    def test_price_action_with_date(self):

        from f_utils import price_action
        import pandas as pd
        import datetime

        start_date = datetime.datetime.today() - datetime.timedelta(1)
        data = price_action(token_path = 
        "../resources/token.txt", ticker = "PLTR", 
        start_date = start_date)

        self.assertTrue(isinstance(data, pd.DataFrame))
        


# run the actual unittests
unittest.main()
