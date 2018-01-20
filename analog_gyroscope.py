from microbit import *

class AnalogGyroscope:
	def __init__(self, pin_input, voltage=3.3, zero_voltage=1.65, sensitivity=0.007):
		self.pin_input = pin_input
		self.voltage = voltage
		self.zero_voltage = zero_voltage
		self.sensitivity = sensitivity

		self.time_last_update = -1
		self.angle = 0

		self.pin_input.read_analog()

	def zero(self, sample_time=0.5):
		time_start = running_time()
		values = []

		while running_time() < time_start + (sample_time/1000):
			values.append(self.pin_input.read_analog())

		self.zero_voltage = sum(values) / len(values) # use average
		self.angle = 0
		self.time_last_update = running_time()

	def get_angle(self):
		return self.angle

	def update(self):
		time_delta = running_time() - self.time_last_update
		if time_delta != 0:
			# calculate angle delta
			rate = self.pin_input.read_analog()
			rate /= 1023
			rate *= self.voltage
			rate -= self.zero_voltage
			rate /= self.sensitivity
			rate /= time_delta
			
			self.angle += rate # apply angle delta

			self.time_last_update = running_time() # remember last update
