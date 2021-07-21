'''
Unit testing my utilities

Cheat Sheet:
https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
'''

#%%
from visualize import Visualize
import unittest

class TestVisualize(unittest.TestCase):
    def test_bar_pyo(self):
        v = Visualize()
        v.bar(x = [1,2,3,4], y = [1,2,3,4], display_type="pyo",
        title = "Dummy Barplot")
    
    def test_onedim_distplot(self):
        v = Visualize()
        v.onedim_distplot(data = [1,2,3,4,4,4,5,6,3,4,5,2,3,2,3,4,1,5,3,3,2],
        title = "Dummy Distplot")
    
    def test_candle(self):
        v = Visualize()
        v.candle()


# run the actual unittests
unittest.main()
