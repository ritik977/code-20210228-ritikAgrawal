import unittest
import sys
sys.path.append('../')
from services import index_cal

class TestIndexCalc(unittest.TestCase):

    def test_bmi_cal(self):
        result = index_cal.bmi_cal(96, 171)
        expected = {"BMI":32.83,"BMI_Category": "Normal_weight", "Health_risk": "low_risk"}
        self.assertEqual(result, expected)