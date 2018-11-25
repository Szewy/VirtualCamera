class Line3D:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def getLines(self):
		list = []
		list.append(self)
		
		return list
    
	def move(self, direction):
		self.a.move(direction)
		self.b.move(direction)
			
	def rotate(self, direction):
		self.a.rotate(direction)
		self.b.rotate(direction)