import unittest
from unittest.mock import Mock, call
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
        sensor = Mock()
        sensor.get_current_temperature.return_value = 50
        # WHEN the fan is controlled
        fan = Mock()
        controller = TemperatureController(sensor, fan)
        controller.regulate_fan_speed()

        # THEN the fan should be set to HIGH speed
        fan.set_fan_speed.assert_called_once_with(FanSpeed.HIGH)


    #def test_fan_blips_once(self):
        # GIVEN a fan is returns the sequence (10, 10, 100, 10, 10)
    def test_fan_follows_temperature_over_time(self):
        # GIVEN a sensor whose temperature changes over time: 20 -> 35 -> 50 -> 20 degC
        sensor = Mock()
        sensor.get_current_temperature.side_effect = [20, 35, 50, 20]
 
        # WHEN the fan is controlled after each temperature reading
        fan = Mock()
        controller = TemperatureController(sensor, fan)
 
        controller.regulate_fan_speed()
        controller.regulate_fan_speed()
        controller.regulate_fan_speed()
        controller.regulate_fan_speed()
 
        # THEN the fan speed should follow the temperature changes
        self.assertEqual(
            fan.set_fan_speed.call_args_list,
            [
                call(FanSpeed.OFF),
                call(FanSpeed.MEDIUM),
                call(FanSpeed.HIGH),
                call(FanSpeed.OFF),
            ],
        )
 
 
        # WHEN the fan is controlled (for 5 times)

        # THEN the FAN follows the blip (OFF, OFF, HIGH, OFF, OFF)

