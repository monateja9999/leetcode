

class Parkingspot():
	def __init__(self, spot_id: str):
		self.spot_id = spot_id
		self.is_parked = False



class Parkinglot():
	def __init__(self, row: int, col: int):
		self.hor = row
		self.ver = col
		self.parking_lot =[[None for _ in range(col)]for _ in range(row)]
		self.create_grid()



	def create_grid(self):
		for i in range(self.hor):
			for j in range(self.ver):
				self.parking_lot[i][j] = Parkingspot(str(i)+'-'+str(j))

	def display_spot_id(self ,row:int, col:int):
		return self.parking_lot[row][col].spot_id


if __name__ == "__main__":

	lot1 = Parkinglot(3,4)
	print(lot1.display_spot_id(1,2))