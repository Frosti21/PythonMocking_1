import unittest
from temp_control import TemperatureController, FanSpeed

class TestTemperatureController(unittest.TestCase):
    def setUp(self):
        # ...
        pass

    def tearDown(self):
        # ...
        pass

    def test_fan_turns_high_at_50_degrees(self):
        # GIVEN a temperature of 50 degC

        # WHEN the fan is controlled

        # THEN the fan should be set to HIGH speed
        self.assertTrue(False)
