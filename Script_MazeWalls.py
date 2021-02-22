import pygame

class MazeWalls():
	def __init__(self, window):
		self.color = (255,0,0)
		self.window = window
		self.walls=[]
		self.wall_4=[685,400,30,100]#4 οκ
		self.wall_2=[600,585,100,30]#2 ok
		self.wall_19=[200,185,100,30]#19 ok
		self.wall_5=[500,485,200,30]#5 ok
		self.wall_11=[300,385,200,30]#11 ok
		self.wall_14=[200,485,200,30]#14 ok
		self.wall_25=[100,585,200,30]#25 ok
		self.wall_18=[0,285,200,30]#18 ok
		self.wall_6=[600,285,100,30]#6 ok
		self.wall_8=[500,185,300,30]#8 ok
		self.wall_23=[400,85,200,30]#23 ok
		self.wall_1=[685,700,30,100]#1 ok
		self.wall_26=[185,700,30,100]#26 ok
		self.wall_3=[585,600,30,200]#3 ok
		self.wall_9=[485,500,30,200]#9 ok
		self.wall_13=[385,500,30,200]#13 ok
		self.wall_15=[285,600,30,200]#15 ok
		self.wall_16=[185,300,30,200]#16 ok
		self.wall_24=[85,400,30,300]#24 ok
		self.wall_21=[85,0,30,200]#21 ok
		self.wall_7=[585,300,30,200]#7 ok
		self.wall_10=[485,200,30,200]#10 ok
		self.wall_17=[285,100,30,300]#17 ok
		self.wall_20=[185,100,30,100]#20 ok
		self.wall_22=[385,0,30,300]#22 ok
		self.wall_12=[400,685,100,30]#12 ok
		self.walls.append(self.wall_1)
		self.walls.append(self.wall_2)
		self.walls.append(self.wall_3)
		self.walls.append(self.wall_4)
		self.walls.append(self.wall_5)
		self.walls.append(self.wall_6)
		self.walls.append(self.wall_7)
		self.walls.append(self.wall_8)
		self.walls.append(self.wall_9)
		self.walls.append(self.wall_10)
		self.walls.append(self.wall_11)
		self.walls.append(self.wall_12)
		self.walls.append(self.wall_13)
		self.walls.append(self.wall_14)
		self.walls.append(self.wall_15)
		self.walls.append(self.wall_16)
		self.walls.append(self.wall_17)
		self.walls.append(self.wall_18)
		self.walls.append(self.wall_19)
		self.walls.append(self.wall_20)
		self.walls.append(self.wall_21)
		self.walls.append(self.wall_22)
		self.walls.append(self.wall_23)
		self.walls.append(self.wall_24)
		self.walls.append(self.wall_25)
		self.walls.append(self.wall_26)
		
	def maze_walls(self):
		pygame.draw.rect(self.window, self.color, [self.wall_1[0], self.wall_1[1], self.wall_1[2] , self.wall_1[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_2[0], self.wall_2[1], self.wall_2[2] , self.wall_2[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_3[0], self.wall_3[1], self.wall_3[2] , self.wall_3[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_4[0], self.wall_4[1], self.wall_4[2] , self.wall_4[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_5[0], self.wall_5[1], self.wall_5[2] , self.wall_5[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_6[0], self.wall_6[1], self.wall_6[2] , self.wall_6[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_7[0], self.wall_7[1], self.wall_7[2] , self.wall_7[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_8[0], self.wall_8[1], self.wall_8[2] , self.wall_8[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_9[0], self.wall_9[1], self.wall_9[2] , self.wall_9[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_10[0], self.wall_10[1], self.wall_10[2] , self.wall_10[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_11[0], self.wall_11[1], self.wall_11[2] , self.wall_11[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_12[0], self.wall_12[1], self.wall_12[2] , self.wall_12[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_13[0], self.wall_13[1], self.wall_13[2] , self.wall_13[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_14[0], self.wall_14[1], self.wall_14[2] , self.wall_14[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_15[0], self.wall_15[1], self.wall_15[2] , self.wall_15[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_16[0], self.wall_16[1], self.wall_16[2] , self.wall_16[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_17[0], self.wall_17[1], self.wall_17[2] , self.wall_17[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_18[0], self.wall_18[1], self.wall_18[2] , self.wall_18[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_19[0], self.wall_19[1], self.wall_19[2] , self.wall_19[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_20[0], self.wall_20[1], self.wall_20[2] , self.wall_20[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_21[0], self.wall_21[1], self.wall_21[2] , self.wall_21[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_22[0], self.wall_22[1], self.wall_22[2] , self.wall_22[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_23[0], self.wall_23[1], self.wall_23[2] , self.wall_23[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_24[0], self.wall_24[1], self.wall_24[2] , self.wall_24[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_25[0], self.wall_25[1], self.wall_25[2] , self.wall_25[3]], 0)
		pygame.draw.rect(self.window, self.color, [self.wall_26[0], self.wall_26[1], self.wall_26[2] , self.wall_26[3]], 0)
		pygame.draw.rect(self.window, (0,255,0), [40, 50, 10 , 10], 0)



		