import pygame
from math import *

class Snake:
	def __init__(self):
		pygame.init()
		self.width = 600
		self.height = 500
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("SNAKE")
		self.clock = pygame.time.Clock()
		self.running = True
		self.snake_width = 300
		self.snake_height = 250
		self.snake_lenght = 30
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.speedx = 0
		self.speedy = 0
		self.gameLoop()

	def gameLoop(self):
		while self.running:
			self.clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.speedx = -5
						self.speedy = 0
					if event.key == pygame.K_DOWN:
						self.speedx = 0
						self.speedy = 5
					if event.key == pygame.K_UP:
						self.speedx = 0
						self.speedy = -5

			self.getUI()
			self.move()

	def initUI(self):
		pygame.draw.rect(self.screen,self.black,(self.snake_width,self.snake_height,self.snake_lenght,5))

	def getUI(self):
		self.screen.fill(self.white)
		self.initUI()
		pygame.display.update()

	def collition(self):
		pass

	def move(self):
		self.snake_width = self.snake_width + self.speedx
		self.snake_height = self.snake_height + self.speedy
		if self.snake_width <= -self.snake_lenght:
			self.snake_width = 600

	def gameOver(self):
		pass

if __name__ == "__main__":
	app = Snake()