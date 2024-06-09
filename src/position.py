
class Position:
	def __init__(self, position_x, position_y):
		self.x = position_x
		self.y = position_y


	def __eq__(self, other):
		return self.x == other.x and self.y == other.y


	def __mul__(self, other):
		return Position(self.x*other, self.y*other)



