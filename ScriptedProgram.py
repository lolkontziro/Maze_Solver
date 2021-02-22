import pygame
import random
from Script_World_2 import World
from Script_MazeWalls import MazeWalls



pygame.init()
display_width = 800
display_height = 800



window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Maze Solver')
fps = pygame.time.Clock()



def text_objects(text, font):
	textSurface = font.render(text, True, (0,0,0))
	return textSurface, textSurface.get_rect()


def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',10)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (60, 20)
	window.blit(TextSurf, TextRect)
	pygame.display.update()



def gen(gener):
	message_display(f'generation: {gener}' )

def walls(posx, posy, wallw, wallh, color):
	wall =pygame.draw.rect(window, color, [posx, posy, wallw, wallh], 0)





def game_loop():
	generation =0
	
	maze = MazeWalls(window)

	
	

	x=(750)
	y=(750)
	world = World(window, 1000, x, y)
	
	close_window = False


	while not close_window:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				close_window = True

			print(event)
		
		
		
		window.fill((255, 255, 255))
		if  world.allDotsDead() == True:
			world.calc_fitness()
			world.natural_Selection()
			world.mutate_Babies()

			generation += 1

		elif generation == 31:
			break


		else:
			maze.maze_walls()
			world.update_world()
			world.draw_world()
			pygame.draw.rect(window, (0,255,0), [700, 100, 10 , 10], 0)
			

			gen(generation)

				
				
			pygame.display.update()
			fps.tick(144)



game_loop() 
pygame.quit()
quit()          







  
