from Script_Dots_2 import Dots
import pygame
import random
from math import sqrt
from Script_MazeWalls import MazeWalls

class DotClone():
	def __init__(self, window):
		self.dots = []
		self.window = window
		self.fitnessSum = float(self.dots.__len__())
		self.all_dead = False
		self.destination_x =0
		self.destination_y =0
		self.stepcount = 40
		self.maze = MazeWalls(self.window)
		self.walls = self.maze.walls


	def add(self, num, x, y):
		for i in range(0 ,num):
			self.dots.append(Dots(x, y, self.stepcount))

	def draw_dots(self):
		for dot in self.dots:
			dot.call(self.window)

	def update_dots(self):
		self.all_Dots_Dead()
		for dot in self.dots:
			if self.is_at_destination(dot):
				dot.update_destination()
				self.destination_x = dot.destination_x
				self.destination_y = dot.destination_y
			
			elif self.is_at_goal(dot):
				dot.reached_goal = True
			elif self.is_at_boundary(dot):
				dot.hit_bound = True
				dot.dead = True
			elif self.is_at_wall(dot):
				dot.wrong_path = True
				dot.dead = True
			
			
			else:
				dot.update_movement()
	
	def is_at_destination(self, dot):
		if sqrt((dot.x - dot.destination_x)**2 +(dot.y - dot.destination_y)**2) < 1:
			return True
		return False

	def is_at_boundary(self, dot):
		if dot.x + dot.dx < 0 or dot.x + dot.dx > 800 :
			return True


		if dot.y + dot.dy < 0 or dot.y + dot.dy > 800 :
			return True
		return False

		
	def calcutaleFitness(self):
		for dot in self.dots:
			dot.calculate_Fitness()

	def all_Dots_Dead(self):
		count = 0
		for dot in self.dots:
			if dot.dead == True or dot.reached_goal== True:
				count += 1
		if count == len(self.dots):
			self.all_dead = True
					

	def is_at_goal(self, dot):
		if dot.distance_To_Goal < 5:
			dot.reached_goal = True
			return True
		return False

	def is_at_wall(self, dot):
		hit = False
		for i in range(len(self.walls)):
			if dot.x >= self.walls[i][0] and dot.x <= (self.walls[i][0]+self.walls[i][2]) and dot.y >= self.walls[i][1] and dot.y <= (self.walls[i][1] + self.walls[i][3]):
				hit = True
				break
			else:
				hit = False
		return hit



	def naturalSelection(self):
		newDots = []
		bestDot = None
		bestBaby = None
		max_fit = 0
		min_run_sequence_count = 3000
		self.calculateFitnessSum()

		for dot in self.dots:
			if dot.fitness > max_fit:
				test_dot = dot
				if test_dot.run_sequence_count < min_run_sequence_count:
					bestDot= test_dot
				max_fit = dot.fitness

			parent = self.selectParent()
			newDots.append(parent.baby(dot.start_x, dot.start_y,self.stepcount))
		bestBaby = bestDot.baby(bestDot.start_x, bestDot.start_y, self.stepcount)
		bestBaby.dotImg.fill((0,255,0))
		newDots[999] = bestBaby 
		for i in  range(len(self.dots)):
			self.dots[i] = newDots[i]
		for dot in self.dots:
			dot.create_run_sequence()
		self.all_dead= False
		if self.stepcount >2400:
			self.stepcount = 2400
		else:
			self.stepcount += 20
		


	def calculateFitnessSum(self):
		for dot in self.dots:
			self.fitnessSum += dot.fitness


	def selectParent(self):
		rand = random.uniform(0.0 ,self.fitnessSum)
		runningSum = 0.0
		new_dot = None

		while new_dot == None:

			for dot in self.dots:
				runningSum += dot. fitness 

				if (runningSum >= rand):
					new_dot = dot
					return new_dot
					break
		return new_dot


	def mutateBabies(self):
		for dot in self.dots:
			dot.mutate()
