class Microwave:
	def __init__(self, brand : str, power_rating: int) -> None:
		self.brand = brand
		self.power_rating = power_rating
		self.turned_on: bool = False 
	
	def turn_on(self) -> None:
		if self.turned_on:
			print(f'Microwave({self.brand}) is already turned on.')
		else:
			self.turned_on = True
			print(f'Microwave({self.brand}) is now turned on.')
	
	def turn_off(self) -> None:
		if self.turned_on:
			self.turned_on = False
			print(f'Microwave({self.brand}) is now turned off.')
		else:
			print(f'Microwave({self.brand}) is already turned off.')

	def run(self, seconds: int) -> None:
		if self.turned_on:
			while seconds > 0:
				print(f'Microwave({self.brand}) is started and will run for {seconds} seconds.')
				seconds -= 1
		else:
			print(f'Microwave({self.brand}) is turned off, Please switch it on to run.')



bosch: Microwave = Microwave("Bosch",1)
smeg: Microwave = Microwave("Smeg",2)

print(smeg)



