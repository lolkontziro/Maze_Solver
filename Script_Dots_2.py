import pygame
import random
from math import sqrt
class Dots():
	def __init__ (self, x, y,step_count):
		self.dotImg = pygame.image.load('dotImg.png')
		self.dead = False
		self.hit_bound = False
		self.start_x = x
		self.start_y = y

		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.destination_x = 0
		self.destination_y = 0
		self.run_sequence_count = 1
		self.acc = 2 
		self.speed = 1
		self.run_sequence = []
		self.run_sequence_length = step_count
		self.counter = - (self.run_sequence_length/4)
		self.max_dist =random.randint(1, 50)
		self.goal_x = 700 #40
		self.goal_y = 100 #50
		self.distance_To_Goal =sqrt((self.goal_x - self.x)**2 + (self.goal_y - self.y)**2)
		self.fitness = 0.0
		self.reached_goal = False
		self.wrong_path = False
		
		self.create_run_sequence()
		self.update_direction()
		self.update_destination()


	def create_run_sequence(self):
		while len(self.run_sequence) < self.run_sequence_length:
			delta_x = random.randint(-self.max_dist,self.max_dist)
			delta_y = random.randint(-self.max_dist, self.max_dist)
			if delta_x != 0 or delta_y != 0:
				self.run_sequence.append((delta_x,delta_y))
				

		

	def call(self, given_surface):
		given_surface.blit(self.dotImg,(self.x,self.y))

	def update_movement(self):
		if not self.dead and not self.reached_goal and not self.hit_bound:
			self.x += self.dx*self.acc
			self.y += self.dy*self.acc
			self.distance_To_Goal =sqrt((self.goal_x - self.x)**2 + (self.goal_y - self.y)**2)
			self.fitness = 0.5/(self.distance_To_Goal * self.distance_To_Goal)

		
		
		
	def update_destination(self):
		if self.run_sequence_count  == len(self.run_sequence) :
			self.dead = True
		else:
			self.run_sequence_count += 1
		self.update_direction()

	

	def update_direction(self):
		self.acc_calculate()
		dx, dy = self.run_sequence[self.run_sequence_count -1]
		self.destination_x = self.x + dx
		self.destination_y = self.y + dy
		magnitude = sqrt(dx**2 + dy**2)
		self.dx = (dx/magnitude) 
		self.dy = (dy/magnitude) 

	def calculate_Fitness(self):
		if self.wrong_path == True:
			self.fitness = 0
		elif self.reached_goal == True:
			self.fitness = 1.0/16.0 + 100000.0/float((self.run_sequence_count-1)*(self.run_sequence_count-1))
		elif self.hit_bound == True:
			self.fitness = 0.000001 *(1.0/(self.distance_To_Goal * self.distance_To_Goal))

		else:
			self.fitness =1.0/(self.distance_To_Goal * self.distance_To_Goal)

	def clone(self):
		clone = Dots(self.x, self.y,self.run_sequence_length)
		for i in range(self.run_sequence_length):
			clone.run_sequence[i] =self.run_sequence[i]
		return clone

	def baby(self, x, y, step_count):
		clone= self.clone()
		baby = Dots(x, y, step_count)
		baby.run_sequence = clone.run_sequence
		return baby

	def mutate(self):
		mutationRate= 0.01
		new_run_sequence = []

		count = 0
		for i in range(self.run_sequence_length):
			rand =random.random()
			if rand <mutationRate:
				dx_dy_zero =True
				while dx_dy_zero == True:
					max_dist =random.randint(1, 100)
					delta_x = random.randint(-max_dist, max_dist)
					delta_y = random.randint(-max_dist, max_dist)
					if delta_x != 0 or delta_y != 0:
						dx_dy_zero = False
						self.run_sequence[i]=((delta_x,delta_y))

	def acc_calculate(self):
		if self.counter == 0:
			self.counter = -(self.run_sequence_length/4)
			self.acc += 1
			








