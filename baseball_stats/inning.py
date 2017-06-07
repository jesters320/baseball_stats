class Inning:

	def __init__(self, input_inning):
		self.this_inning = input_inning
		self.at_bat_count = 0
	
	def add_at_bat(self):
		self.at_bat_count += 1
	
	def remove_at_bat(self):
		self.at_bat_count -= 1