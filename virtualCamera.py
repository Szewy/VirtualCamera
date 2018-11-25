import perspectiveProjection
import cohenSutherland
import point2D

class VirtualCamera:	
	perspectiveProjection  = perspectiveProjection.PerspectiveProjection()
	
	def zoomOut(self):
		self.d = self.d * 2.0

	def zoomIn(self):
		self.d = self.d / 2.0
	
	def __init__(self, observator, d, width, height):
		self.observator = observator
		self.d = d
		self.width = width
		self.height = height
		self.cohenSutherland = cohenSutherland.CohenSutherland(point2D.Point2D(0, 0), width, height)
	
	def calculate(self, object3Ds):
		lineList = []
		
		for obj in object3Ds:
			lineList = lineList + obj.getLines()
			
		lineList2D = self.perspectiveProjection.project(lineList, self.d)
		
		visibleLines2D = self.cohenSutherland.trimLines(lineList2D)
		return visibleLines2D
		
		#return lineList2D
        