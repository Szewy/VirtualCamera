import pygame, sys,os
import virtualWorld
import cube
import point3D
import point2D
import line2D
import directionEnum

from pygame.locals import *

pygame.init()

windowHeight = 600
windowWidth = 600

window = pygame.display.set_mode((windowWidth, windowHeight))

GREEN = (20,220,10)

virtualWorld = virtualWorld.VirtualWorld()

cube1 = cube.Cube(point3D.Point3D(-2.0, 0.0, 10.0), 3.0)
cube2 = cube.Cube(point3D.Point3D(2.0, 0.0, 10.0), 3.0)
cube3 = cube.Cube(point3D.Point3D(-2.0, 0.0, 5.0), 3.0)
cube4 = cube.Cube(point3D.Point3D(2.0, 0.0, 5.0), 3.0)

virtualWorld.addElement(cube1)
virtualWorld.addElement(cube2)
virtualWorld.addElement(cube3)
virtualWorld.addElement(cube4)

def scale(lines):
	cameraHeight = virtualWorld.virtualCamera.height
	cameraWidth = virtualWorld.virtualCamera.width

	heightScale = windowHeight / cameraHeight
	widthScale = windowWidth / cameraWidth

	output = [];

	for line in lines:
		a = point2D.Point2D(windowWidth / 2 + line.a.x * widthScale, windowHeight / 2 - line.a.y * heightScale)
		b = point2D.Point2D(windowWidth / 2 + line.b.x * widthScale, windowHeight / 2 - line.b.y * heightScale)
		newLine = line2D.Line2D(a,b)
		output.append(newLine)
	
	return output
		
def drawLine(line2D):
	x1 = line2D.a.x
	x2 = line2D.b.x
	y1 = line2D.a.y
	y2 = line2D.b.y
	
	pygame.draw.line(window, GREEN, (x1, y1), (x2, y2), 1)
	
def drawLines(lines):
	for line in lines:
		drawLine(line)
		
def draw():
	window.fill((0,0,0))
	lines2D = virtualWorld.generate2D()
	scaledLines2D = scale(lines2D)
	drawLines(scaledLines2D)
	
def input(events):
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				virtualWorld.move(directionEnum.DirectionEnum.RIGHT)
			elif event.key == pygame.K_RIGHT:
				virtualWorld.move(directionEnum.DirectionEnum.LEFT)
			elif event.key == pygame.K_UP:
				virtualWorld.move(directionEnum.DirectionEnum.DOWN)
			elif event.key == pygame.K_DOWN:
				virtualWorld.move(directionEnum.DirectionEnum.UP)
			elif event.key == pygame.K_t:
				virtualWorld.move(directionEnum.DirectionEnum.BACKWARD)
			elif event.key == pygame.K_y:
				virtualWorld.move(directionEnum.DirectionEnum.FORWARD)
				
			elif event.key == pygame.K_p:
				virtualWorld.zoomOut()
			elif event.key == pygame.K_m:
				virtualWorld.zoomIn()
				
			elif event.key == pygame.K_d:
				virtualWorld.rotate(directionEnum.DirectionEnum.RIGHT)
			elif event.key == pygame.K_a:
				virtualWorld.rotate(directionEnum.DirectionEnum.LEFT)
			elif event.key == pygame.K_w:
				virtualWorld.rotate(directionEnum.DirectionEnum.DOWN)
			elif event.key == pygame.K_s:
				virtualWorld.rotate(directionEnum.DirectionEnum.UP)
			elif event.key == pygame.K_z:
				virtualWorld.rotate(directionEnum.DirectionEnum.BACKWARD)
			elif event.key == pygame.K_x:
				virtualWorld.rotate(directionEnum.DirectionEnum.FORWARD)
	
while True:
	input(pygame.event.get())
	draw()
	pygame.display.update()