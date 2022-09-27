import copy
import numpy as np
import pygame
from pygame.locals import *
import random


size = surface_width, surface_height = 1400, 800 
num_cols = surface_width // 10
num_rows = surface_height // 10
block_size =  surface_width // num_cols
black = pygame.Color("black")
alive_colour = (100, 149, 237)
dead_colour = (33, 33, 33)
fps = 30

def make_array():

    # create random array

    array = np.zeros([num_cols, num_rows])
    for i in range(num_cols):
        for j in range(num_rows):
            array[i][j] = random.randint(0, 1)

    return array

def count_neighbours(array, x, y):

    # cycling through the array, counting the number of living cells that surround each cell in the array

    neighbours = 0
    for i in range(-1,2):
        for j in range(-1,2):
            neighbours += array[(i + x + num_cols) % num_cols][(j + y + num_rows) % num_rows] 
               
    neighbours -= array[x][y]     
    return neighbours

def rules(array):

    # deepcopy array and apply rules to the current array, creating the new array

    next_array = copy.deepcopy(array)
    for i in range(num_cols):
        for j in range(num_rows):

            count = count_neighbours(array, i, j)
            state = array[i][j]

            if state == 1 and count > 3:
                next_array[i][j] = 0
            elif state == 1 and count < 2:
                next_array[i][j] = 0
            elif state == 0 and count == 3:
                next_array[i][j] = 1
    
    array = next_array
    return array

def main():

    # open pygame and initialise surface

    pygame.init()
    pygame.display.set_caption("Welcome to John Conway's Game Of Life")
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    surface.fill(black)

    # create initial array

    array = make_array()

    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                        
                    
    # draw the array of blocks

        for i in range(num_cols):
            for j in range(num_rows):
                if array[i][j] == 1:
                    pygame.draw.rect(surface, alive_colour, (i * block_size, j * block_size, block_size - 1, block_size -1))
                else:
                    pygame.draw.rect(surface, dead_colour, (i * block_size, j * block_size, block_size - 1, block_size -1))
                                
        array = rules(array)
                        
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()

