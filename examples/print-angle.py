from microbit import *
from analog_gyroscope import AnalogGyroscope

gyro = AnalogGyroscope(pin0)

while True:
	gyro.update()
	print(gyro.get_angle())
	sleep(100)