import unittest
from app.calculate_distance.routes import get_distance
from app.config import Config


class CalculateDistanceTestCase(unittest.TestCase):
    def test_get_distance(self):
        
        self.assertEqual(get_distance("Çankaya, Ankara, Turkey"), 1528.8362963925294)

        self.assertEqual(get_distance("Khoroshyovo-Mnyovniki District"), Config.TARGET_IN_MKAD_MESSAGE)

        self.assertEqual(get_distance("Alkpolsoiyf dadsfasd"), Config.ERROR_MESSAGE)