import unittest
import sys
sys.path.insert(1,"/Users/mtaruno/Documents/DevZone/Utilities/")
import finance_utils as f_utils


token_path = "/Users/mtaruno/Documents/DevZone/Utilities/resources/token.txt"

class TestFinanceUtils(unittest.TestCase):

    def test_price_action(self):
        import pandas as pd
        data = f_utils.price_action(token_path = token_path, ticker = "PLTR")
        print(data.head())
        self.assertTrue(isinstance(data, pd.DataFrame))

    def test_price_action_with_date(self):
        import pandas as pd
        import datetime

        start_date = datetime.datetime.today() - datetime.timedelta(1)

        data = f_utils.price_action(token_path = token_path, ticker = "PLTR", 
        start_date = start_date)

        self.assertTrue(isinstance(data, pd.DataFrame))
        

    def test_multi_price_action(self):
        tickers = ['MARA','TSLA','CHPT']
        import datetime
        start_date = datetime.datetime.today() - datetime.timedelta(1)
        data = f_utils.multi_price_action(tickers, token_path = token_path)
        print(data)
        
# run the actual unittests
unittest.main()
