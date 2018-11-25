import point2D
import line2D

class PerspectiveProjection:
	def projectPoint2D(self, pointD, d):
		return point2D.Point2D(pointD.x * d / pointD.z, pointD.y * d / pointD.z)

	def projectLine2D(self, line, d):
		return line2D.Line2D(self.projectPoint2D(line.a, d), self.projectPoint2D(line.b, d))

	def project(self, line3Ds, d):
		line2Ds = []
		
		for line in line3Ds:
			line2Ds.append(self.projectLine2D(line, d))
		
		return line2Ds