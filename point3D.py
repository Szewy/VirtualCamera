import directionEnum
import math

class Point3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
	def move(self, direction):
		if direction == directionEnum.DirectionEnum.UP:
			self.y = self.y + 1;
		elif direction == directionEnum.DirectionEnum.DOWN:
			self.y = self.y - 1;
		elif direction == directionEnum.DirectionEnum.LEFT:
			self.x = self.x - 1;
		elif direction == directionEnum.DirectionEnum.RIGHT:
			self.x = self.x + 1;
		elif direction == directionEnum.DirectionEnum.FORWARD:
			self.z = self.z + 1;
		elif direction == directionEnum.DirectionEnum.BACKWARD:
			self.z = self.z - 1;
			
	def rotate(self, direction):
		angle = 0.1

		if direction == directionEnum.DirectionEnum.UP:
			y2 = self.y;
			z2 = self.z;
			self.y = y2 * math.cos(angle) - z2* math.sin(angle);
			self.z = y2 * math.sin(angle) + z2* math.cos(angle);
		elif direction == directionEnum.DirectionEnum.DOWN:
			y2 = self.y;
			z2 = self.z;
			self.y = y2 * math.cos(-angle) - z2 * math.sin(-angle);
			self.z = y2 * math.sin(-angle) + z2 * math.cos(-angle);
		elif direction == directionEnum.DirectionEnum.LEFT:
			x2 = self.x;
			z2 = self.z;
			self.x = x2 * math.cos(angle) + z2 * math.sin(angle);
			self.z = -1 * x2 * math.sin(angle) + z2 * math.cos(angle);
		elif direction == directionEnum.DirectionEnum.RIGHT:
			x2 = self.x;
			z2 = self.z;
			self.x = x2 * math.cos(-angle) + z2 * math.sin(-angle);
			self.z = -1 * x2 * math.sin(-angle) + z2 * math.cos(-angle);
		elif direction == directionEnum.DirectionEnum.FORWARD:
			x2 = self.x;
			y2 = self.y;
			self.x = x2 * math.cos(-angle) - y2 * math.sin(-angle);
			self.y = x2 * math.sin(-angle) + y2 * math.cos(-angle);
		elif direction == directionEnum.DirectionEnum.BACKWARD:
			x2 = self.x;
			y2 = self.y;
			self.x = x2 * math.cos(angle) - y2 * math.sin(angle);
			self.y = x2 * math.sin(angle) + y2 * math.cos(angle);
		