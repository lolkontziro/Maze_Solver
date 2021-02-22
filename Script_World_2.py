from Script_Clone_2 import DotClone
from math import sqrt
from random import randint

class World():
	def __init__(self, window, num_dots, x , y):
		self.x = x
		self.y = y
		self.dots = DotClone(window)
		self.init(num_dots)
	
	def init(self, num_dots):
		self.dots.add(num_dots, self.x, self.y)
	
	def update_world(self):
		self.dots.update_dots()

		
	def draw_world(self):
		self.dots.draw_dots()

	def calc_fitness(self):
		self.dots.calcutaleFitness()

	def natural_Selection(self):
		self.dots.naturalSelection()

	def allDotsDead(self):
		return self.dots.all_dead

	def mutate_Babies(self):
		self.dots.mutateBabies()
