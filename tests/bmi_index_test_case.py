import unittest
import sys
sys.path.append('../')
from services import bmi_index

class TestBmiIndex(unittest.TestCase):

    def test_bmi_table(self):
        result = bmi_index.bmi_table()
        #print('res', result)
        
        self.assertTrue(result)

    def test_cal_overweight_people(self):
        result = bmi_index.cal_overweight_people()
        #print('res', result)
        
        self.assertTrue(result)