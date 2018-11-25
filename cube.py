import line3D
import point3D

class Cube:
	lines = []
	
	def __init__(self, middle, sideLength):
		self.lowerBase(middle, sideLength)
		self.upperBase(middle, sideLength)
		self.sides(middle, sideLength)
	
	def move(self, direction):
		for line in self.lines:
			line.move(direction)

	def rotate(self, direction):
		for line in self.lines:
			line.rotate(direction)
	
	def lowerBase(self, middle, sideLength):
		half = sideLength / 2.0

		line = line3D.Line3D(point3D.Point3D(middle.x-half, middle.y-half, middle.z - half), point3D.Point3D(middle.x - half, middle.y - half, middle.z + half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x - half, middle.y - half, middle.z - half), point3D.Point3D(middle.x + half, middle.y - half, middle.z - half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y - half, middle.z + half), point3D.Point3D(middle.x - half, middle.y - half, middle.z + half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y - half, middle.z + half), point3D.Point3D(middle.x + half, middle.y - half, middle.z - half))
		self.lines.append(line)
        
	def upperBase(self, middle, sideLength):
		half = sideLength / 2.0

		line = line3D.Line3D(point3D.Point3D(middle.x - half, middle.y + half, middle.z - half), point3D.Point3D(middle.x - half, middle.y + half, middle.z+ half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x - half, middle.y + half, middle.z - half), point3D.Point3D(middle.x + half, middle.y + half, middle.z - half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y + half, middle.z + half), point3D.Point3D(middle.x - half, middle.y + half, middle.z + half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y + half, middle.z + half), point3D.Point3D(middle.x + half, middle.y + half, middle.z - half))
		self.lines.append(line)

	def sides(self, middle, sideLength):
		half = sideLength / 2.0

		line = line3D.Line3D(point3D.Point3D(middle.x - half, middle.y + half, middle.z - half), point3D.Point3D(middle.x - half, middle.y - half, middle.z - half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x - half, middle.y + half, middle.z + half), point3D.Point3D(middle.x - half, middle.y - half, middle.z + half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y + half, middle.z - half), point3D.Point3D(middle.x + half, middle.y - half, middle.z - half))
		self.lines.append(line)

		line = line3D.Line3D(point3D.Point3D(middle.x + half, middle.y + half, middle.z + half), point3D.Point3D(middle.x + half, middle.y - half, middle.z + half))
		self.lines.append(line)
		
	def getLines(self):
		return self.lines