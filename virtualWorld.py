import virtualCamera
import point3D

class VirtualWorld:
	objects = []
	virtualCamera = virtualCamera.VirtualCamera(point3D.Point3D(0.0, 0.0, 0.0), 0.5, 2.0, 2.0)
		
	def addElement(self, obj):
		self.objects.append(obj)
		
	def generate2D(self):
		return self.virtualCamera.calculate(self.objects)
	
	def move(self, direction):
		for obj in self.objects:
			obj.move(direction)

	def rotate(self, direction):
		for obj in self.objects:
			obj.rotate(direction)

	def zoomIn(self):
		self.virtualCamera.zoomIn()

	def zoomOut(self):
		self.virtualCamera.zoomOut()