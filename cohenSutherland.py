import point2D
import line2D

class CohenSutherland:
	def  __init__(self, middlePoint, width, height):
		self.middlePoint = middlePoint
		self.width = width
		self.height = height
		self.left = middlePoint.x - self.width / 2
		self.right = middlePoint.x + self.width / 2
		self.bottom = middlePoint.y - self.height / 2
		self.top = middlePoint.y + self.height / 2

	def trimLine(self, line):
		return self.cohen(line.a.x, line.a.y, line.b.x, line.b.y)

	def trimLines(self, lines):
		drawLines = []
		
		for line in lines:
			drawLine = self.trimLine(line)
			
			if drawLine != None:
				drawLines.append(drawLine)
		
		return drawLines
	
	def calcRegCode(self, x, y):
		result = 0;

		if x < self.left:
			result |= 0x1
		if x > self.right:
			result |= 0x2
		if y > self.top:
			result |= 0x8
		if y < self.bottom:
			result |= 0x4

		return result

	def cohen(self, x1, y1, x2, y2):
		rcode1 = self.calcRegCode(x1, y1)
		rcode2 = self.calcRegCode(x2, y2)

		if (rcode1 & rcode2) != 0:
			return None
		elif (rcode1 | rcode2) == 0:
			a = point2D.Point2D(x1, y1)
			b = point2D.Point2D(x2, y2)
			drawLine = line2D.Line2D(a, b)
			return drawLine
		else:
			while True:
				x = x1
				y = y1

				if rcode1 != 0:
					rcode = rcode1
				else:
					rcode = rcode2

				if (rcode & 0x1) != 0:
					y = y1 + (y2 - y1) * (self.left - x1) / (x2 - x1)
					x = self.left
				elif (rcode & 0x2) != 0:
					y = y1 + (y2 - y1) * (self.right - x1) / (x2 - x1)
					x = self.right
				elif (rcode & 0x4) != 0:
					x = x1 + (x2 - x1) * (self.bottom - y1) / (y2 - y1)
					y = self.bottom
				elif (rcode & 0x8) != 0:
					x = x1 + (x2 - x1) * (self.top - y1) / (y2 - y1)
					y = self.top

				if rcode == rcode1:
					x1 = x
					y1 = y
					rcode1 = self.calcRegCode(x1, y1)
				else:
					x2 = x
					y2 = y
					rcode2 = self.calcRegCode(x2, y2)
				
				if not ((rcode1 & rcode2) == 0 and (rcode1 | rcode2) != 0):
					break;

			if (rcode1 | rcode2) == 0:
				a = point2D.Point2D(x1, y1)
				b = point2D.Point2D(x2, y2)
				drawLine = line2D.Line2D(a, b)
				return drawLine
		
		return None;