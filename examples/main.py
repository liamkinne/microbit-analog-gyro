from microbit import *
from analog_gyroscope import AnalogGyroscope

gyro = AnalogGyroscope(pin0)

while True:
	print(gyro.get_angle())