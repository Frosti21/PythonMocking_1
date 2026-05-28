import unittest
from temp_control import TemperatureController, FanSpeed

class MockTemperaturSensor():
    def __init__(self, temp):
        self.temperature = temp
        
    def get_current_temperature(self):
        return self.temperature


class MockFan():
    def set_fan_speed(self, speed):
        self.last_speed = speed
    

    def get_last_speed(self):
        return self.get_last_speed



class TestTemperatureController(unittest.TestCase):
    def setUp(self):
        # ...
        pass

    def tearDown(self):
        # ...
        pass

    def test_fan_turns_high_at_50_degrees(self):
        # GIVEN a temperature of 50 degC
        sensor = MockTemperaturSensor(50)
        fan = MockFan()
        # WHEN the fan is controlled
        ctl = TemperatureController( sensor, fan)
        ctl.regulate_fan_speed()

        # THEN the fan should be set to HIGH speed
        self.assertTrue(fan.get_last_speed) == FanSpeed.HIGH

    def test_fan_blips_once(self):
        # GIVEN