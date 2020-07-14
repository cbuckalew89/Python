import pygame
import os
from pygame import *
from os import *

class Vehicle:
	VEH_IMAGE_NORMAL = pygame.image.load(os.path.join('data', 'crapbt.png'))
	def __init__(self):
		self.vehicle = self.VEH_IMAGE_NORMAL.convert_alpha()
		self.image = self.vehicle
		self.x = 100
		self.y = 100
		self.heading = 0
		
	def update(self):
		pass
		
	def turn_left(self):
		self.heading = self.heading - 90
		self._constrainHeading()
		
	def turn_right(self):
		self.heading = self.heading + 90
		self._constrainHeading()
		
	def forward(self):
		if ((self.heading == 0)or(self.heading == 360)):
			self.y -= 100
		elif (self.heading == 90):
			self.x += 100
		elif (self.heading == 180):
			self.y += 100
		elif (self.heading == 270):
			self.x -= 100
			
	def _constrainHeading(self):
		if self.heading < 0:
			self.heading = 270
		elif self.heading > 360:
			self.heading = 90
		
	def draw(self, surface):
		rot_image = pygame.transform.rotate(self.image, -self.heading)
		rect = rot_image.get_rect()
		rect.center = (self.x,self.y)
		surface.blit(rot_image, rect)	
	

class BigTrak:
	def __init__(self):
		display.init()
		display.set_caption('Big Trak')
		self.screen = display.set_mode((1024, 768))
		self.gameEndCode = 0
		self.vehicles = []
		self.vehicles.append(Vehicle())
		
        pass
        
	def start(self):
		clock = pygame.time.Clock()
		
		while (self.gameEndCode == 0):
			pygame.display.flip()
			for event in pygame.event.get():
				if(event.type == pygame.KEYDOWN): 
					if(event.key == pygame.K_ESCAPE):
						self.gameEndCode = 1
					elif (event.key == pygame.K_RIGHT):
						self.vehicles[0].turn_right()
					elif (event.key == pygame.K_LEFT):
						self.vehicles[0].turn_left()
					elif (event.key == pygame.K_UP):
						self.vehicles[0].forward()
			pygame.draw.rect(self.screen, (255, 255, 255), self.screen.get_rect())
			self.vehicles[0].draw(self.screen)
				

def main():
	b = BigTrak()
	b.start()
	return 0

if __name__ == '__main__':
	main()
© 2020 GitHub, Inc.
