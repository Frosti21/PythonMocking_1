import unittest
from temp_control import TemperatureController, FanSpeed

class MockTemperatureSensor:
    """Fake temperature sensor that returns a preset temperature."""
    def __init__(self, temperature):
        self.temperature = temperature

    def get_current_temperature(self):
        return self.temperature


class MockFanControl:
    """Fake fan control that records every commanded speed."""
    def __init__(self):
        self.last_speed = None
        self.speed_history = []

    def set_fan_speed(self, speed):
        self.last_speed = speed
        self.speed_history.append(speed)


class TestTemperatureController(unittest.TestCase):
    def test_fan_turns_high_at_50_degrees(self):
        # GIVEN a temperature of 50 degC
        sensor = MockTemperatureSensor(50)

        # WHEN the fan is controlled
        fan = MockFanControl()
        controller = TemperatureController(sensor, fan)
        controller.regulate_fan_speed()

        # THEN the fan should be set to HIGH speed
        self.assertEqual(fan.last_speed, FanSpeed.HIGH)

    def test_fan_turns_medium_at_35_degrees(self):
        # GIVEN a temperature of 35 degC
        sensor = MockTemperatureSensor(35)

        # WHEN the fan is controlled
        fan = MockFanControl()
        controller = TemperatureController(sensor, fan)
        controller.regulate_fan_speed()

        # THEN the fan should be set to MEDIUM speed
        self.assertEqual(fan.last_speed, FanSpeed.MEDIUM)

    def test_fan_turns_off_at_20_degrees(self):
        # GIVEN a temperature of 20 degC
        sensor = MockTemperatureSensor(20)

        # WHEN the fan is controlled
        fan = MockFanControl()
        controller = TemperatureController(sensor, fan)
        controller.regulate_fan_speed()

        # THEN the fan should be turned OFF
        self.assertEqual(fan.last_speed, FanSpeed.OFF)

    def test_fan_follows_temperature_over_time(self):
        # GIVEN a sensor whose temperature changes over time: 20 -> 35 -> 50 -> 20 degC
        sensor = MockTemperatureSensor(20)

        # WHEN the fan is controlled after each temperature change
        fan = MockFanControl()
        controller = TemperatureController(sensor, fan)

        controller.regulate_fan_speed()
        sensor.temperature = 35
        controller.regulate_fan_speed()
        sensor.temperature = 50
        controller.regulate_fan_speed()
        sensor.temperature = 20
        controller.regulate_fan_speed()

        # THEN the fan speed should follow the temperature changes
        self.assertEqual(
            fan.speed_history,
            [FanSpeed.OFF, FanSpeed.MEDIUM, FanSpeed.HIGH, FanSpeed.OFF],
        )