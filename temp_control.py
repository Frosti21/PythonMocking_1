import time
import random

class FanSpeed:
    HIGH = 100
    MEDIUM = 50
    LOW = 20
    OFF = 0

class TemperatureController:
    """
    Controls a fan's speed based on the current temperature.
    This class depends on external methods to get the temperature and set fan speed.
    """
    def __init__(self, temperature_sensor, fan_control):
        self.temperature_sensor = temperature_sensor
        self.fan_control = fan_control

    def regulate_fan_speed(self):
        """
        Fetches the current temperature and sets the fan speed accordingly.
        """
        current_temp = self.temperature_sensor.get_current_temperature()
        print(f"Current temperature: {current_temp}°C")

        if current_temp > 40:
            self.fan_control.set_fan_speed(FanSpeed.HIGH)

        elif current_temp > 25:
            self.fan_control.set_fan_speed(FanSpeed.MEDIUM)

        elif current_temp > 20:
            self.fan_control.set_fan_speed(FanSpeed.LOW) 

        else:
            self.fan_control.set_fan_speed(FanSpeed.OFF)




class RealTemperatureSensor:
    """
    A hypothetical real temperature sensor that might interact with hardware.
    """
    def get_current_temperature(self):
        # In a real scenario, this would read from a sensor.
        # For demonstration, let's return a simulated value.
        return 25 + random.randint(-10, 20)  # Example temperature

class RealFanControl:
    """
    A hypothetical real fan control system that interacts with fan hardware.
    """
    def set_fan_speed(self, speed):
        # In a real scenario, this would send a command to the fan.
        print(f"Commanding fan to speed: {speed}")

